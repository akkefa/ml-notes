"""Tests for the memory write side + session benchmark (Notebook 10).

Offline only: a ``HashingEmbedder`` gives deterministic dedup similarities and a
scripted ``FakeModel`` drives the no-memory baseline, so the harness mechanics
are exercised without any model download.
"""
from __future__ import annotations

from types import SimpleNamespace

from llmlab.evals.sessions import (
    FACT_BANK,
    answer_from_window,
    make_sessions,
    render_window,
)
from llmlab.memory.store import MemoryStore
from llmlab.memory.writer import MemoryWriter
from llmlab.retrieval.embeddings import HashingEmbedder
from llmlab.retrieval.retrievers import DenseRetriever

INC_A = "Incident INC-3071 was caused by a memory leak in the websocket handler."
INC_B = "Incident INC-4188 was caused by a memory leak in the websocket handler."


class FakeModel:
    def __init__(self, scripted):
        self.scripted = list(scripted)
        self.i = 0

    def generate(self, messages, sampling=None, **_):
        text = self.scripted[min(self.i, len(self.scripted) - 1)]
        self.i += 1
        return SimpleNamespace(text=text, new_tokens=max(1, len(text.split())))


# --- write-all -------------------------------------------------------------
def test_write_all_stores_everything():
    writer = MemoryWriter(MemoryStore(), HashingEmbedder(dim=4096))
    for f in FACT_BANK[:5]:
        assert writer.write(f.statement).stored
    assert len(writer.store) == 5


# --- dedup -----------------------------------------------------------------
def test_dedup_drops_exact_duplicate():
    writer = MemoryWriter(MemoryStore(), HashingEmbedder(dim=4096), dedup_threshold=0.95)
    first = writer.write("the wifi password is rocket-42")
    again = writer.write("the wifi password is rocket-42")
    assert first.stored
    assert not again.stored and again.merged_into == first.record.id
    assert len(writer.store) == 1


def test_dedup_threshold_controls_confusable_merge():
    """The confusable-cluster trap: two incidents differ only by an opaque ID.
    A loose threshold merges them (losing the ID); a tight one keeps both."""
    loose = MemoryWriter(MemoryStore(), HashingEmbedder(dim=4096), dedup_threshold=0.9)
    loose.write(INC_A)
    assert not loose.write(INC_B).stored        # ~0.92 cosine -> merged away
    assert len(loose.store) == 1

    tight = MemoryWriter(MemoryStore(), HashingEmbedder(dim=4096), dedup_threshold=0.95)
    tight.write(INC_A)
    assert tight.write(INC_B).stored            # distinct ID survives
    assert len(tight.store) == 2


# --- capacity / forgetting -------------------------------------------------
def test_capacity_evicts_oldest():
    writer = MemoryWriter(MemoryStore(), HashingEmbedder(dim=4096), capacity=3)
    results = [writer.write(f.statement) for f in FACT_BANK[:5]]
    assert len(writer.store) == 3
    assert results[3].evicted == results[0].record.id   # FIFO: first in, first out
    assert results[4].evicted == results[1].record.id
    # a retriever built after eviction sees only the survivors
    retriever = DenseRetriever(writer.store, HashingEmbedder(dim=4096))
    assert len(retriever.records) == 3


# --- sessions --------------------------------------------------------------
def test_sessions_are_deterministic_and_distinct():
    a = make_sessions(n_sessions=3, n_facts=6, spacing=2, seed=0)
    b = make_sessions(n_sessions=3, n_facts=6, spacing=2, seed=0)
    assert [t.text for t in a[0].turns] == [t.text for t in b[0].turns]
    facts = a[0].facts
    assert len({f.answer for f in facts}) == len(facts)   # distinct answers in a session


def test_recall_distance_decreases_with_position():
    session = make_sessions(n_sessions=1, n_facts=5, spacing=2, seed=1)[0]
    items = session.recall_items()
    distances = [d for _, d in items]
    assert distances == sorted(distances, reverse=True)   # earliest fact is furthest
    assert len(session.turns) == 5 * (1 + 2)


def test_render_window_slices_recent_turns():
    session = make_sessions(n_sessions=1, n_facts=4, spacing=1, seed=2)[0]
    text = render_window(session.turns, window=3)
    assert text.count("\n") == 2                          # 3 lines -> 2 newlines
    last_turn = session.turns[-1].text
    assert last_turn in text


def test_answer_from_window_returns_text_and_tokens():
    session = make_sessions(n_sessions=1, n_facts=3, spacing=1, seed=3)[0]
    model = FakeModel(["I don't know"])
    text, tokens = answer_from_window(model, session.turns, "anything?", window=4)
    assert text == "I don't know" and tokens >= 1
