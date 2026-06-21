"""The manual ReAct loop — no framework (Notebook 07).

    task -> [system + scratchpad] -> model -> parse JSON action -> run tool
         -> append observation -> repeat -> final_answer

Every step is recorded in a ``Trace`` so the whole decision process is
inspectable. The model only ever sees a *canonical* re-serialised action as its
own turn, so a rambling generation or a hallucinated "Observation:" can't poison
later steps.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from llmlab.agent.parsing import extract_json
from llmlab.agent.prompts import build_system_prompt
from llmlab.agent.tools import FINAL_ANSWER, ToolRegistry

_BAD_JSON_OBS = (
    "Error: respond with ONE JSON object containing the keys 'thought', 'tool', and 'args'."
)


@dataclass
class Step:
    thought: Optional[str]
    tool: Optional[str]
    args: Optional[dict]
    observation: Optional[str]
    raw: str


@dataclass
class AgentResult:
    answer: Optional[str]
    success: bool
    steps: int
    total_new_tokens: int
    trace: list = field(default_factory=list)
    messages: list = field(default_factory=list)


class Agent:
    def __init__(self, model, registry: ToolRegistry, max_steps: int = 6,
                 sampling=None, few_shot: bool = True, nudge_on_repeat: bool = True,
                 system_prompt: Optional[str] = None, prose_is_final: bool = False):
        self.model = model
        self.registry = registry
        self.max_steps = max_steps
        self.nudge_on_repeat = nudge_on_repeat
        # prose_is_final: small models often break protocol and *blurt the answer*
        # in plain text once they have it. When True, a non-tool generation that
        # follows at least one tool call is accepted as the final answer instead of
        # being rejected — a pragmatic robustness valve (Notebook 09 measures it).
        self.prose_is_final = prose_is_final
        # An explicit system_prompt (e.g. the memory agent's) overrides the default
        # arithmetic-flavoured one built from the registry.
        self.system_prompt = system_prompt or build_system_prompt(registry, few_shot=few_shot)
        if sampling is None:
            from llmlab.models.local_model import SamplingConfig

            sampling = SamplingConfig(max_new_tokens=200)
        self.sampling = sampling

    def run(self, task: str) -> AgentResult:
        import json

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": task},
        ]
        trace: list[Step] = []
        seen: set[str] = set()
        total_tokens = 0
        tool_calls = 0

        for _ in range(self.max_steps):
            result = self.model.generate(messages, self.sampling)
            total_tokens += getattr(result, "new_tokens", 0)
            action = extract_json(result.text)

            if not isinstance(action, dict) or "tool" not in action:
                answer_text = result.text.strip()
                if self.prose_is_final and tool_calls >= 1 and answer_text:
                    trace.append(Step(None, None, None, None, result.text))
                    return AgentResult(answer_text, True, len(trace), total_tokens, trace, messages)
                trace.append(Step(None, None, None, _BAD_JSON_OBS, result.text))
                messages.append({"role": "assistant", "content": answer_text[:300]})
                messages.append({"role": "user", "content": f"Observation: {_BAD_JSON_OBS}"})
                continue

            thought = action.get("thought")
            tool = action.get("tool")
            args = action.get("args", {})
            # canonical assistant turn keeps the scratchpad clean
            messages.append({
                "role": "assistant",
                "content": json.dumps({"thought": thought, "tool": tool, "args": args}),
            })

            if tool == FINAL_ANSWER:
                answer = args.get("answer", "") if isinstance(args, dict) else args
                trace.append(Step(thought, tool, args, None, result.text))
                return AgentResult(str(answer).strip(), True, len(trace), total_tokens, trace, messages)

            observation = self.registry.call(tool, args)
            tool_calls += 1
            # loop guard: small models re-issue the same call instead of finishing
            signature = json.dumps([tool, args], sort_keys=True, default=str)
            if self.nudge_on_repeat and signature in seen:
                observation = (
                    f"{observation}. You have already computed this; do not repeat it. "
                    "If it answers the question, respond with final_answer now."
                )
            seen.add(signature)
            trace.append(Step(thought, tool, args, observation, result.text))
            messages.append({"role": "user", "content": f"Observation: {observation}"})

        return AgentResult(None, False, len(trace), total_tokens, trace, messages)


# --- evaluation adapter (reuses the Notebook 06 scorer) --------------------
@dataclass
class AgentEvalRecord:
    task_id: str
    category: str
    gold: float
    pred: Optional[float]
    correct: bool
    success: bool
    steps: int
    new_tokens: int
    answer: Optional[str]


def evaluate_agent(agent: Agent, tasks) -> list:
    """Run the agent on each task and score its final answer like any strategy."""
    from llmlab.evals.extract import extract_answer, is_correct

    records = []
    for task in tasks:
        result = agent.run(task.question)
        pred = extract_answer(result.answer) if result.answer is not None else None
        records.append(AgentEvalRecord(
            task_id=task.id,
            category=task.category,
            gold=float(task.answer),
            pred=pred,
            correct=is_correct(pred, task.answer),
            success=result.success,
            steps=result.steps,
            new_tokens=result.total_new_tokens,
            answer=result.answer,
        ))
    return records
