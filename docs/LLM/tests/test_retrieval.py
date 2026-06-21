"""Tests for the memory store + retrieval stack (Notebook 08).

Offline tests use the deterministic ``HashingEmbedder`` so all retrieval
mechanics (store, dense, BM25, hybrid fusion, metrics) run with no downloads.
One ``slow`` test asserts genuine *semantic* retrieval with the real model.
"""
from __future__ import annotations

import pytest

from llmlab.memory.corpus import RETRIEVAL_PROBES, SAMPLE_MEMORIES, build_sample_store
from llmlab.memory.store import MemoryRecord, MemoryStore
from llmlab.retrieval.embeddings import HashingEmbedder
from llmlab.retrieval.metrics import evaluate_retriever, mrr_at_k, recall_at_k
from llmlab.retrieval.retrievers import (
    BM25Retriever,
    DenseRetriever,
    HybridRetriever,
    default_tokenize,
)


# --- store -----------------------------------------------------------------
def test_store_add_get_and_autoids():
    store = MemoryStore()
    a = store.add("first note")
    b = store.add("second note", kind="episodic", metadata={"x": 1})
    assert a.id == "m001" and b.id == "m002"
    assert store.get("m002").kind == "episodic" and store.get("m002").metadata == {"x": 1}
    assert len(store) == 2 and store.texts() == ["first note", "second note"]


def test_store_add_many_and_rejects_duplicates():
    store = MemoryStore()
    store.add_many(SAMPLE_MEMORIES)
    assert len(store) == len(SAMPLE_MEMORIES)
    assert store.get("m16").text.startswith("The user takes their coffee")
    with pytest.raises(ValueError):
        store.add("dup", id="m16")


def test_store_jsonl_roundtrip(tmp_path):
    store = build_sample_store()
    path = store.save_jsonl(tmp_path / "mem.jsonl")
    reloaded = MemoryStore.load_jsonl(path)
    assert reloaded.ids() == store.ids()
    assert reloaded.get("m20").text == store.get("m20").text


# --- hashing embedder ------------------------------------------------------
def test_hashing_embedder_shapes_and_determinism():
    emb = HashingEmbedder(dim=64)
    vecs = emb.encode(["hello world", "hello world", "totally different tokens"])
    assert vecs.shape == (3, 64)
    assert (vecs[0] == vecs[1]).all()                       # deterministic
    assert abs(float((vecs[0] * vecs[0]).sum()) - 1.0) < 1e-5  # L2-normalised


# --- dense / bm25 ----------------------------------------------------------
def test_dense_retriever_ranks_exact_text_first():
    store = build_sample_store()
    dense = DenseRetriever(store, HashingEmbedder())
    target = store.get("m07").text
    hits = dense.search(target, k=3)
    assert hits[0].id == "m07" and hits[0].score > 0.99
    assert len(dense.search(target, k=2)) == 2


def test_bm25_finds_rare_token():
    store = build_sample_store()
    bm25 = BM25Retriever(store)
    assert bm25.search("DB_STAGING_PW", k=1)[0].id == "m04"
    assert bm25.search("INC-2055", k=1)[0].id == "m20"


def test_default_tokenize_splits_identifiers():
    assert default_tokenize("DB_STAGING_PW") == ["db", "staging", "pw"]
    assert default_tokenize("ACME-7781!") == ["acme", "7781"]
    assert default_tokenize("error E1042") == ["error", "e1042"]


# --- hybrid ----------------------------------------------------------------
def test_hybrid_rrf_combines_both_retrievers():
    store = build_sample_store()
    dense = DenseRetriever(store, HashingEmbedder())
    bm25 = BM25Retriever(store)
    hybrid = HybridRetriever(dense, bm25, method="rrf")
    hits = hybrid.search("DB_STAGING_PW", k=3)
    assert hits[0].id == "m04" and 1 <= len(hits) <= 3


def test_hybrid_linear_method_runs():
    store = build_sample_store()
    hybrid = HybridRetriever(
        DenseRetriever(store, HashingEmbedder()), BM25Retriever(store),
        method="linear", alpha=0.5,
    )
    hits = hybrid.search("Kubernetes version", k=5)
    assert hits and "m15" in [h.id for h in hits]


def test_hybrid_gate_drops_zero_score_lexical_pollution():
    store = build_sample_store()
    # High dim -> effectively collision-free token buckets, so only memories that
    # truly share a token with the query get a non-zero dense score.
    dense = DenseRetriever(store, HashingEmbedder(dim=4096))
    bm25 = BM25Retriever(store)
    query = "DB_STAGING_PW"  # db/staging/pw appear only in m04
    gated = HybridRetriever(dense, bm25, gate=True).search(query, k=5)
    naive = HybridRetriever(dense, bm25, gate=False).search(query, k=5)
    assert all(h.id == "m04" for h in gated)      # gating keeps only real matches
    assert len(naive) > len(gated)                # naive pads with zero-overlap memories


# --- metrics ---------------------------------------------------------------
def test_recall_and_mrr():
    assert recall_at_k(["a", "b", "c"], {"b"}, 2) == 1.0
    assert recall_at_k(["a", "b", "c"], {"d"}, 2) == 0.0
    assert recall_at_k(["a", "b"], {"a", "b"}, 1) == 0.5
    assert mrr_at_k(["a", "b"], {"b"}, 5) == 0.5
    assert mrr_at_k(["a", "b"], {"z"}, 5) == 0.0


def test_evaluate_retriever_report():
    store = build_sample_store()
    bm25 = BM25Retriever(store)
    report = evaluate_retriever(bm25, RETRIEVAL_PROBES, k=3)
    assert report.n == len(RETRIEVAL_PROBES)
    assert 0.0 <= report.recall_at_k <= 1.0
    cats = report.recall_by_category()
    assert set(cats) == {"paraphrase", "exact-term", "mixed"}
    # BM25 should ace the rare-token probes:
    assert cats["exact-term"] > 0.9


def test_corpus_probes_reference_real_memories():
    ids = {m[0] for m in SAMPLE_MEMORIES}
    assert len(ids) == len(SAMPLE_MEMORIES)  # unique ids
    for probe in RETRIEVAL_PROBES:
        assert probe.relevant_ids <= ids
        assert probe.kind in {"paraphrase", "exact-term", "mixed"}


# --- slow: genuine semantic retrieval with the real model ------------------
@pytest.mark.slow
def test_dense_retriever_is_semantic():
    from llmlab import config
    from llmlab.retrieval.embeddings import Embedder

    config.configure_caches()
    embedder = Embedder()
    assert embedder.dim == 384
    dense = DenseRetriever(build_sample_store(), embedder)
    # paraphrase with zero shared content words must still find the coffee note:
    hits = dense.search("How do I like my morning beverage prepared?", k=3)
    assert "m16" in [h.id for h in hits]
