"""Tests for the reasoning-eval harness (Notebook 06).

Extraction, prompts, and the task set are pure and tested offline. The harness
itself is exercised against tiny SmolLM2-135M (marked ``slow``) — we assert
*structure* (valid accuracy, full records), not that a 135M model is smart.
"""
from __future__ import annotations

import pytest

from llmlab.evals.extract import extract_answer, is_correct
from llmlab.evals.prompts import cot_messages, direct_messages, fewshot_cot_messages
from llmlab.evals.tasks import FEWSHOT_EXEMPLARS, GSM_TASKS

TINY = "HuggingFaceTB/SmolLM2-135M-Instruct"


# --- extraction ------------------------------------------------------------
def test_extract_prefers_answer_cue_over_intermediate_numbers():
    assert extract_answer("First 24 - 9 = 15, then 15 - 7 = 8. The answer is 8.") == 8.0


def test_extract_handles_marker_commas_and_bare_number():
    assert extract_answer("#### 1,234") == 1234.0
    assert extract_answer("26") == 26.0
    assert extract_answer("blah 3 + 5 = 8") == 8.0  # last-number fallback


def test_extract_returns_none_without_numbers():
    assert extract_answer("I don't know") is None
    assert extract_answer("") is None


def test_is_correct_tolerates_float_form():
    assert is_correct(8.0, 8) is True
    assert is_correct(None, 8) is False
    assert is_correct(7.0, 8) is False


# --- prompts ---------------------------------------------------------------
def test_direct_and_cot_message_shapes():
    direct = direct_messages("What is 2+2?")
    assert direct[0]["role"] == "system" and "2+2" in direct[-1]["content"]
    cot = cot_messages("What is 2+2?")
    assert "step by step" in cot[-1]["content"].lower()


def test_fewshot_includes_exemplar_turns():
    messages = fewshot_cot_messages("Q?", FEWSHOT_EXEMPLARS)
    # system + 2 turns per exemplar + final user question
    assert len(messages) == 1 + 2 * len(FEWSHOT_EXEMPLARS) + 1
    assert messages[-1]["content"] == "Q?"
    assert messages[1]["role"] == "user" and messages[2]["role"] == "assistant"


# --- task set --------------------------------------------------------------
def test_task_set_is_well_formed():
    assert len(GSM_TASKS) >= 10
    ids = [t.id for t in GSM_TASKS]
    assert len(ids) == len(set(ids))  # unique
    assert all(isinstance(t.answer, int) for t in GSM_TASKS)


# --- slow harness ----------------------------------------------------------
@pytest.fixture(scope="module")
def lm():
    from llmlab import config
    from llmlab.models.local_model import LocalModel

    config.configure_caches()
    return LocalModel(TINY)


@pytest.mark.slow
def test_evaluate_returns_report(lm):
    from llmlab.evals.harness import evaluate
    from llmlab.models.local_model import SamplingConfig

    report = evaluate(lm, GSM_TASKS[:2], direct_messages, "direct",
                      sampling=SamplingConfig(max_new_tokens=16))
    assert report.n == 2
    assert 0.0 <= report.accuracy <= 1.0
    assert len(report.records) == 2


@pytest.mark.slow
def test_self_consistency_majority_vote(lm):
    from llmlab.evals.harness import self_consistency

    report = self_consistency(lm, GSM_TASKS[:1], cot_messages, k=3, max_new_tokens=64)
    assert report.n == 1
    assert isinstance(report.records[0].correct, bool)
