"""Non-agentic RAG baselines (Notebook 09).

Two reference points the agentic retriever must beat:

* ``closed_book_answer`` — no memory at all; the model answers from its weights.
* ``static_rag_answer``  — always retrieve top-k for the raw question, stuff the
  notes into the prompt, answer once. Simple, strong, and the bar to clear.

Both return the model's raw text so the same scorer judges every condition.
"""
from __future__ import annotations

from llmlab.models.local_model import SamplingConfig

CLOSED_BOOK_SYSTEM = (
    "Answer the question in one short sentence. "
    "If you are not sure of the answer, reply exactly: I don't know."
)

GROUNDED_SYSTEM = (
    "Answer the question using ONLY the notes provided below. "
    "The notes must actually match the question (e.g. the same ID). "
    "If the notes do not contain the answer, reply exactly: I don't know."
)

RELEVANCE_SYSTEM = "You are a strict relevance checker. Reply with only one word: yes or no."


def closed_book_answer(model, question: str, sampling=None):
    """Answer with no memory. Returns ``(text, new_tokens)``."""
    messages = [
        {"role": "system", "content": CLOSED_BOOK_SYSTEM},
        {"role": "user", "content": question},
    ]
    result = model.generate(messages, sampling or SamplingConfig(max_new_tokens=64))
    return result.text.strip(), result.new_tokens


def static_rag_answer(model, retriever, question: str, k: int = 3, sampling=None):
    """Retrieve top-k, inject as notes, answer once. Returns ``(text, hits, new_tokens)``."""
    hits = retriever.search(question, k)
    notes = "\n".join(f"- {h.text}" for h in hits) if hits else "(no notes found)"
    messages = [
        {"role": "system", "content": GROUNDED_SYSTEM},
        {"role": "user", "content": f"Notes:\n{notes}\n\nQuestion: {question}"},
    ]
    result = model.generate(messages, sampling or SamplingConfig(max_new_tokens=64))
    return result.text.strip(), hits, result.new_tokens


def is_relevant(model, question: str, note: str, sampling=None):
    """Ask the model whether a note actually answers the question. Returns ``(bool, new_tokens)``."""
    user = (
        f"Question: {question}\nNote: \"{note}\"\n"
        "Does this note state the answer to the question? "
        "Any ID, code, or name in the question must appear in the note. Answer yes or no."
    )
    result = model.generate(
        [{"role": "system", "content": RELEVANCE_SYSTEM}, {"role": "user", "content": user}],
        sampling or SamplingConfig(max_new_tokens=4),
    )
    return result.text.strip().lower().startswith("y"), result.new_tokens


def gated_rag_answer(model, retriever, question: str, k: int = 3, sampling=None):
    """Retrieve, then *check relevance* before answering; abstain if the top note
    doesn't match. The minimal 'agentic' decision that works at 0.5B.
    Returns ``(text, hits, new_tokens)``."""
    hits = retriever.search(question, k)
    if not hits:
        return "I don't know", hits, 0
    relevant, gate_tokens = is_relevant(model, question, hits[0].text)
    if not relevant:
        return "I don't know", hits, gate_tokens
    messages = [
        {"role": "system", "content": GROUNDED_SYSTEM},
        {"role": "user", "content": f"Notes:\n- {hits[0].text}\n\nQuestion: {question}"},
    ]
    result = model.generate(messages, sampling or SamplingConfig(max_new_tokens=48))
    return result.text.strip(), hits, gate_tokens + result.new_tokens
