"""Tests for the from-scratch agent (Notebook 07).

A ``FakeModel`` returns scripted generations so the *entire* loop — happy path,
malformed-JSON recovery, hallucinated tools, non-termination, and the scoring
adapter — is tested deterministically with no LLM. One ``slow`` test drives the
loop with a real model.
"""
from __future__ import annotations

import pytest

from llmlab.agent.loop import Agent, AgentResult, evaluate_agent
from llmlab.agent.parsing import extract_json
from llmlab.agent.prompts import build_system_prompt
from llmlab.agent.tools import calculate, make_default_registry
from llmlab.evals.tasks import GSM_TASKS


class _FakeResult:
    def __init__(self, text: str, new_tokens: int = 12):
        self.text = text
        self.new_tokens = new_tokens


class FakeModel:
    """Replays scripted outputs; repeats the last one once exhausted."""

    def __init__(self, scripted):
        self.scripted = list(scripted)
        self.calls = 0

    def generate(self, messages, sampling=None):
        idx = min(self.calls, len(self.scripted) - 1)
        self.calls += 1
        return _FakeResult(self.scripted[idx])


# --- safe calculator -------------------------------------------------------
def test_calculate_arithmetic():
    assert calculate("24 - 9 - 7") == 8
    assert calculate("3 * 12 - 10") == 26
    assert calculate("2 ** 5") == 32
    assert calculate("17 // 5") == 3


def test_calculate_rejects_code_and_names():
    for malicious in ("__import__('os')", "open('x')", "x + 1"):
        with pytest.raises(Exception):
            calculate(malicious)


# --- JSON extraction -------------------------------------------------------
def test_extract_json_handles_fences_prose_and_nesting():
    assert extract_json('{"tool": "x"}')["tool"] == "x"
    assert extract_json('Thought... {"a": 1} trailing')["a"] == 1
    assert extract_json('```json\n{"tool": "calculator", "args": {"expression": "2+2"}}\n```')["tool"] == "calculator"
    assert extract_json('{"tool": "t", "args": {"k": 1}}')["args"]["k"] == 1
    assert extract_json('{"n": 1} {"n": 2}')["n"] == 1  # first valid wins
    assert extract_json("no json") is None
    assert extract_json("") is None


# --- registry --------------------------------------------------------------
def test_registry_dispatch_and_error_messages():
    registry = make_default_registry()
    assert registry.call("calculator", {"expression": "24 - 9 - 7"}) == "8"
    assert registry.call("calculator", {"expression": "7^6"}) == "117649"  # ^ -> **
    assert "unknown tool" in registry.call("wikipedia", {})
    assert "object" in registry.call("calculator", "not-a-dict")
    assert "expression" in registry.call("calculator", {})


def test_system_prompt_lists_tools():
    prompt = build_system_prompt(make_default_registry())
    assert "calculator" in prompt and "final_answer" in prompt and "JSON" in prompt


# --- the loop (deterministic, no LLM) --------------------------------------
def test_agent_happy_path():
    model = FakeModel([
        '{"thought": "subtract", "tool": "calculator", "args": {"expression": "24 - 9 - 7"}}',
        '{"thought": "done", "tool": "final_answer", "args": {"answer": "8"}}',
    ])
    result = Agent(model, make_default_registry(), max_steps=5).run("…")
    assert result.success and result.answer == "8"
    assert result.steps == 2
    assert result.trace[0].tool == "calculator" and result.trace[0].observation == "8"


def test_agent_recovers_from_malformed_json():
    model = FakeModel([
        "I think it's 8, let me just say that.",  # no JSON object
        '{"thought": "calc", "tool": "calculator", "args": {"expression": "2 + 3"}}',
        '{"thought": "done", "tool": "final_answer", "args": {"answer": "5"}}',
    ])
    result = Agent(model, make_default_registry(), max_steps=5).run("…")
    assert result.success and result.answer == "5"
    assert result.trace[0].tool is None and "JSON" in result.trace[0].observation


def test_agent_handles_hallucinated_tool():
    model = FakeModel([
        '{"thought": "look it up", "tool": "wikipedia", "args": {"q": "x"}}',
        '{"thought": "done", "tool": "final_answer", "args": {"answer": "42"}}',
    ])
    result = Agent(model, make_default_registry(), max_steps=5).run("…")
    assert "unknown tool" in result.trace[0].observation
    assert result.answer == "42"


def test_agent_stops_at_max_steps_without_final_answer():
    model = FakeModel(['{"thought": "loop", "tool": "calculator", "args": {"expression": "1 + 1"}}'])
    result = Agent(model, make_default_registry(), max_steps=3).run("…")
    assert result.success is False and result.steps == 3


def test_evaluate_agent_scores_against_gold():
    model = FakeModel(['{"thought": "d", "tool": "final_answer", "args": {"answer": "8"}}'])
    records = evaluate_agent(Agent(model, make_default_registry(), max_steps=3), GSM_TASKS[:2])
    assert len(records) == 2
    assert records[0].correct is True   # t01 gold == 8
    assert records[1].correct is False  # t02 gold == 26


# --- slow: a real model drives the loop ------------------------------------
@pytest.mark.slow
def test_agent_runs_with_real_model():
    from llmlab import config
    from llmlab.models.local_model import LocalModel, SamplingConfig

    config.configure_caches()
    model = LocalModel("Qwen/Qwen2.5-0.5B-Instruct", dtype="float32", attn_implementation="sdpa")
    agent = Agent(model, make_default_registry(), max_steps=5,
                  sampling=SamplingConfig(max_new_tokens=160))
    result = agent.run("What is 12 multiplied by 9, minus 7?")
    assert isinstance(result, AgentResult)
    assert result.steps >= 1 and result.total_new_tokens > 0
