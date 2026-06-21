"""The agent's system prompt — the ReAct protocol, spelled out (Notebook 07).

We use a strict one-JSON-object-per-step contract (rather than free-form
``Thought:/Action:``) because it is far easier for a small model to follow and
for us to parse. Tool specs are rendered from the registry so the prompt and the
executable tools never drift apart.

A *worked trajectory* (``few_shot=True``) is included by default. Small models
otherwise tend to re-issue the same calculation forever instead of finishing;
showing the full calculator -> Observation -> ``final_answer`` pattern teaches
them to terminate. Notebook 07 toggles this flag to measure its effect.
"""
from __future__ import annotations

from llmlab.agent.tools import ToolRegistry

_FEWSHOT = [
    "Here is a complete example. The JSON lines are yours; the 'Observation:' line comes from the tool:",
    "",
    "User: What is 6 times 7?",
    '{"thought": "multiply 6 and 7", "tool": "calculator", "args": {"expression": "6 * 7"}}',
    "Observation: 42",
    '{"thought": "the calculator gave 42, so I am done", "tool": "final_answer", "args": {"answer": "42"}}',
]


def build_system_prompt(registry: ToolRegistry, few_shot: bool = True) -> str:
    lines = [
        "You are a problem-solving agent that calls tools to reach an answer.",
        "At each step output EXACTLY ONE JSON object and nothing else — no prose, no markdown, no code fences.",
        "",
        "The JSON object must have exactly these keys:",
        '  "thought": a short reasoning string,',
        '  "tool": the name of one tool to call,',
        '  "args": an object holding that tool\'s arguments.',
        "",
        "Available tools:",
    ]
    lines += [f"- {tool.name}: {tool.description} args: {tool.args_hint}" for tool in registry.tools()]
    lines += [
        "",
        "Rules:",
        "- Use the calculator for ALL arithmetic; never do mental math.",
        "- Take ONE step at a time, then wait for the 'Observation:' before continuing.",
        "- Do NOT repeat a calculation you have already done.",
        "- As soon as an Observation gives you the number you need, call final_answer with just that number.",
    ]
    if few_shot:
        lines += ["", *_FEWSHOT]
    else:
        lines += [
            "",
            "Example of a single step:",
            '{"thought": "I should add 2 and 3", "tool": "calculator", "args": {"expression": "2 + 3"}}',
        ]
    return "\n".join(lines)


# --- memory / retrieval agent (Notebook 09) --------------------------------
_MEMORY_FEWSHOT = [
    "Here are two complete examples. The JSON lines are yours; 'Observation:' comes from the tool:",
    "",
    "User: What timezone does the user work in?",
    '{"thought": "look up the user\'s timezone in memory", "tool": "retrieve", "args": {"query": "user timezone"}}',
    "Observation: [1] (m12) The user lives in Karachi and works in the UTC+5 timezone.",
    '{"thought": "the memory states UTC+5", "tool": "final_answer", "args": {"answer": "UTC+5"}}',
    "",
    "User: What is the user's blood type?",
    '{"thought": "search memory for a blood type", "tool": "retrieve", "args": {"query": "user blood type"}}',
    "Observation: [1] (m06) The user is allergic to peanuts and avoids them when ordering lunch.",
    '{"thought": "no retrieved memory states a blood type", "tool": "final_answer", "args": {"answer": "I don\'t know"}}',
]


def build_memory_system_prompt(registry: ToolRegistry, few_shot: bool = True) -> str:
    """ReAct prompt for a memory-grounded QA agent: retrieve, then answer or abstain."""
    lines = [
        "You are a question-answering agent with access to a long-term memory.",
        "At each step output EXACTLY ONE JSON object and nothing else — no prose, no markdown, no code fences.",
        "",
        "The JSON object must have exactly these keys:",
        '  "thought": a short reasoning string,',
        '  "tool": the name of one tool to call,',
        '  "args": an object holding that tool\'s arguments.',
        "",
        "Available tools:",
    ]
    lines += [f"- {tool.name}: {tool.description} args: {tool.args_hint}" for tool in registry.tools()]
    lines += [
        "",
        "Rules:",
        "- First use retrieve ONCE to look in memory; never answer from your own knowledge.",
        "- Put any specific identifier (like INC-2055 or ACME-7781) verbatim into your query.",
        "- After the Observation, DECIDE — do not search again. Base your answer ONLY on the notes.",
        "- A retrieved memory must MATCH the question (e.g. the SAME ID). A note about a different ID does NOT answer it.",
        "- If a note matches, call final_answer with the answer; if none matches, call final_answer with exactly \"I don't know\".",
    ]
    if few_shot:
        lines += ["", *_MEMORY_FEWSHOT]
    return "\n".join(lines)
