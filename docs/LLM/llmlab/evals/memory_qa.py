"""Memory-QA tasks + a grounding/abstention scorer (Notebook 09).

Questions are grounded in the Notebook 08 corpus and split three ways:

* ``answerable`` — the fact is in the store; the right behaviour is to answer it.
* ``near-miss``  — a *non-existent* ID inside a confusable cluster; retrieval will
  return a real-but-wrong sibling, so the right behaviour is to **abstain**.
* ``far-miss``   — a topic absent from the store; retrieval returns junk -> abstain.

Scoring judges free text into ``correct`` / ``wrong`` / ``abstain``, which lets us
measure not just accuracy but the **hallucination** rate — does a small model
make something up when memory has no answer?
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MemoryQATask:
    id: str
    question: str
    answers: tuple   # accepted answer substrings (lowercase); empty if unanswerable
    answerable: bool
    kind: str        # answerable | near-miss | far-miss


MEMORY_QA_TASKS: list[MemoryQATask] = [
    # answerable — the fact is in the store
    MemoryQATask("a01", "What caused incident INC-2055?", ("websocket",), True, "answerable"),
    MemoryQATask("a02", "How does the user take their coffee?", ("black",), True, "answerable"),
    MemoryQATask("a03", "What latency target does Project Aurora have?", ("200",), True, "answerable"),
    MemoryQATask("a04", "What timezone does the user work in?", ("utc+5", "utc +5"), True, "answerable"),
    MemoryQATask("a05", "What is the lab's default embedding model?", ("minilm",), True, "answerable"),
    MemoryQATask("a06", "What is the user allergic to?", ("peanut",), True, "answerable"),
    MemoryQATask("a07", "What did customer ACME-7781 report?", ("504",), True, "answerable"),
    MemoryQATask("a08", "How do you rotate the API token?", ("rotate-token",), True, "answerable"),
    # near-miss — non-existent ID inside a confusable cluster (retrieval lies)
    MemoryQATask("n01", "What caused incident INC-9999?", (), False, "near-miss"),
    MemoryQATask("n02", "What caused incident INC-1000?", (), False, "near-miss"),
    MemoryQATask("n03", "What did customer ACME-0000 report?", (), False, "near-miss"),
    MemoryQATask("n04", "What did customer ACME-4242 report?", (), False, "near-miss"),
    # far-miss — topic absent from the store
    MemoryQATask("f01", "What is the user's phone number?", (), False, "far-miss"),
    MemoryQATask("f02", "What car does the user drive?", (), False, "far-miss"),
    MemoryQATask("f03", "Who is the user's manager?", (), False, "far-miss"),
    MemoryQATask("f04", "What is the office WiFi password?", (), False, "far-miss"),
]


_ABSTAIN_MARKERS = (
    "i don't know", "i do not know", "don't know", "do not know", "dont know",
    "no relevant", "no memory", "no note", "not in the", "does not contain",
    "doesn't contain", "cannot find", "can't find", "no information",
    "not found", "not provided", "not available", "not mentioned", "n/a",
)


def is_abstention(text: str) -> bool:
    low = (text or "").lower()
    return any(marker in low for marker in _ABSTAIN_MARKERS)


def contains_answer(text: str, answers) -> bool:
    low = (text or "").lower()
    return any(a.lower() in low for a in answers)


def score_memory_answer(text: str, task: MemoryQATask) -> str:
    """Return 'correct', 'wrong', or 'abstain'."""
    if task.answerable:
        if contains_answer(text, task.answers):
            return "correct"
        return "abstain" if is_abstention(text) else "wrong"
    # unanswerable: abstaining is the only correct behaviour
    return "correct" if is_abstention(text) else "wrong"


@dataclass
class MemoryQARecord:
    task_id: str
    kind: str
    answerable: bool
    text: str
    outcome: str
    new_tokens: int
    steps: int


def run_condition(answer_fn, tasks=MEMORY_QA_TASKS) -> list:
    """``answer_fn(task) -> (text, new_tokens, steps)`` for one condition."""
    records = []
    for task in tasks:
        text, new_tokens, steps = answer_fn(task)
        records.append(MemoryQARecord(
            task_id=task.id, kind=task.kind, answerable=task.answerable,
            text=text, outcome=score_memory_answer(text, task),
            new_tokens=new_tokens, steps=steps,
        ))
    return records


def summarize(records) -> dict:
    answerable = [r for r in records if r.answerable]
    unanswerable = [r for r in records if not r.answerable]

    def frac(rows, outcome):
        return sum(r.outcome == outcome for r in rows) / len(rows) if rows else 0.0

    return {
        "answerable_acc": frac(answerable, "correct"),
        "answerable_wrong": frac(answerable, "wrong"),
        "unanswerable_abstain": frac(unanswerable, "correct"),
        "hallucination": frac(unanswerable, "wrong"),
        "avg_tokens": sum(r.new_tokens for r in records) / len(records) if records else 0.0,
        "avg_steps": sum(r.steps for r in records) / len(records) if records else 0.0,
    }
