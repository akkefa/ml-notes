"""Tests for the retrieval-augmented agent stack (Notebook 09).

Offline only: a scripted ``FakeModel`` drives the agent loop and a
``HashingEmbedder``-backed retriever provides deterministic memory, so the whole
read-side memory agent is exercised without any model download.
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest

from llmlab.agent.loop import Agent
from llmlab.agent.prompts import build_memory_system_prompt
from llmlab.agent.rag import closed_book_answer, gated_rag_answer, static_rag_answer
from llmlab.agent.retrieval_tool import format_hits, make_memory_registry, make_retrieve_tool
from llmlab.evals.memory_qa import (
    MEMORY_QA_TASKS,
    MemoryQATask,
    contains_answer,
    is_abstention,
    run_condition,
    score_memory_answer,
    summarize,
)
from llmlab.memory.corpus import build_sample_store
from llmlab.retrieval.embeddings import HashingEmbedder
from llmlab.retrieval.retrievers import DenseRetriever


class FakeModel:
    """Replays scripted assistant turns; ignores the prompt."""

    def __init__(self, scripted):
        self.scripted = list(scripted)
        self.i = 0

    def generate(self, messages, sampling=None, **_):
        text = self.scripted[min(self.i, len(self.scripted) - 1)]
        self.i += 1
        return SimpleNamespace(text=text, new_tokens=max(1, len(text.split())))


def _retriever():
    return DenseRetriever(build_sample_store(), HashingEmbedder(dim=4096))


# --- retrieve tool ---------------------------------------------------------
def test_retrieve_tool_returns_numbered_hits():
    tool = make_retrieve_tool(_retriever(), k=3)
    obs = tool.run({"query": "INC-2055"})
    assert "(m20)" in obs and obs.startswith("[1]")


def test_retrieve_tool_requires_query():
    tool = make_retrieve_tool(_retriever())
    assert "query" in tool.run({})


def test_format_hits_empty():
    assert "No memories" in format_hits([])


def test_memory_registry_has_retrieve_and_final_answer():
    reg = make_memory_registry(_retriever())
    assert set(reg.names()) == {"retrieve", "final_answer"}
    assert reg.call("final_answer", {"answer": "I don't know"}) == "I don't know"


# --- agent loop over memory ------------------------------------------------
def test_agent_retrieves_then_answers():
    reg = make_memory_registry(_retriever(), k=3)
    model = FakeModel([
        '{"thought": "look it up", "tool": "retrieve", "args": {"query": "INC-2055"}}',
        '{"thought": "found it", "tool": "final_answer", "args": {"answer": "a memory leak in the websocket handler"}}',
    ])
    agent = Agent(model, reg, system_prompt=build_memory_system_prompt(reg))
    result = agent.run("What caused incident INC-2055?")
    assert result.success and "websocket" in result.answer
    assert result.steps == 2
    assert "(m20)" in result.trace[0].observation


def test_agent_prose_is_final_accepts_blurted_answer():
    reg = make_memory_registry(_retriever(), k=2)
    model = FakeModel([
        '{"thought": "look", "tool": "retrieve", "args": {"query": "INC-2055"}}',
        "It was a memory leak in the websocket handler.",  # blurted prose, no JSON
    ])
    agent = Agent(model, reg, prose_is_final=True, system_prompt=build_memory_system_prompt(reg))
    result = agent.run("What caused incident INC-2055?")
    assert result.success and "websocket" in result.answer


def test_prose_not_final_before_any_tool_call():
    reg = make_memory_registry(_retriever())
    model = FakeModel(["just chatting, no json here", "still no json"])
    agent = Agent(model, reg, max_steps=2, prose_is_final=True,
                  system_prompt=build_memory_system_prompt(reg))
    result = agent.run("What caused incident INC-2055?")
    assert not result.success  # never retrieved -> prose is not accepted as final


# --- non-agentic baselines (scripted model) -------------------------------
def test_closed_book_static_and_gated_baselines():
    retriever = _retriever()
    assert closed_book_answer(FakeModel(["I don't know"]), "q")[0] == "I don't know"

    text, hits, _ = static_rag_answer(FakeModel(["A memory leak in the websocket handler."]),
                                      retriever, "What caused incident INC-2055?", k=2)
    assert "websocket" in text and hits

    # gate says yes -> answers; gate says no -> abstains
    yes_text, _, _ = gated_rag_answer(FakeModel(["yes", "websocket leak"]), retriever,
                                      "What caused incident INC-2055?", k=2)
    assert "websocket" in yes_text
    no_text, _, _ = gated_rag_answer(FakeModel(["no"]), retriever,
                                     "What caused incident INC-9999?", k=2)
    assert is_abstention(no_text)


def test_agent_can_abstain():
    reg = make_memory_registry(_retriever(), k=2)
    model = FakeModel([
        '{"thought": "search", "tool": "retrieve", "args": {"query": "blood type"}}',
        '{"thought": "nothing matches", "tool": "final_answer", "args": {"answer": "I don\'t know"}}',
    ])
    agent = Agent(model, reg, system_prompt=build_memory_system_prompt(reg))
    result = agent.run("What is the user's blood type?")
    assert result.success and is_abstention(result.answer)


# --- scoring ---------------------------------------------------------------
def test_scoring_outcomes():
    answerable = MemoryQATask("x", "q", ("websocket",), True, "answerable")
    unanswerable = MemoryQATask("y", "q", (), False, "near-miss")
    assert score_memory_answer("It was a websocket leak.", answerable) == "correct"
    assert score_memory_answer("I don't know.", answerable) == "abstain"
    assert score_memory_answer("It was a power outage.", answerable) == "wrong"
    assert score_memory_answer("I don't know.", unanswerable) == "correct"
    assert score_memory_answer("It was a DNS issue.", unanswerable) == "wrong"


def test_abstention_and_contains_helpers():
    assert is_abstention("Sorry, I don't know that.")
    assert not is_abstention("The answer is coffee.")
    assert contains_answer("served black", ("black",))
    assert not contains_answer("served with milk", ("black",))


def test_task_set_is_balanced():
    answerable = [t for t in MEMORY_QA_TASKS if t.answerable]
    unanswerable = [t for t in MEMORY_QA_TASKS if not t.answerable]
    assert len(answerable) == 8 and len(unanswerable) == 8
    assert all(t.answers for t in answerable)
    assert all(not t.answers for t in unanswerable)


def test_run_condition_and_summarize():
    # a perfect oracle: answers answerable with the gold token, abstains otherwise
    def oracle(task):
        text = task.answers[0] if task.answerable else "I don't know"
        return text, 5, 1
    summary = summarize(run_condition(oracle, MEMORY_QA_TASKS))
    assert summary["answerable_acc"] == 1.0
    assert summary["unanswerable_abstain"] == 1.0
    assert summary["hallucination"] == 0.0
