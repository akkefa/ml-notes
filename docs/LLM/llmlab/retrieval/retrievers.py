"""Dense, lexical, and hybrid retrievers over a MemoryStore (Notebook 08).

All three share one interface — ``search(query, k) -> list[Hit]`` — so they are
directly comparable on the same store. Dense uses exact cosine over a normalised
matrix (transparent; FAISS would only matter past ~10^4 items). Lexical uses
BM25. Hybrid fuses the two, by reciprocal rank fusion (default) or normalised
linear score combination.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable, List

import numpy as np

from llmlab.memory.store import MemoryRecord, MemoryStore

_TOKEN_RE = re.compile(r"[a-z0-9]+")


def default_tokenize(text: str) -> list:
    """Lowercase, split on non-alphanumerics — so DB_STAGING_PW and ACME-7781
    become matchable tokens while E1042 / v1.29 stay intact."""
    return _TOKEN_RE.findall(text.lower())


@dataclass
class Hit:
    record: MemoryRecord
    score: float

    @property
    def id(self) -> str:
        return self.record.id

    @property
    def text(self) -> str:
        return self.record.text


class DenseRetriever:
    name = "dense"

    def __init__(self, store: MemoryStore, embedder):
        self.store = store
        self.embedder = embedder
        self.records: List[MemoryRecord] = store.all()
        if self.records:
            self.matrix = embedder.encode([r.text for r in self.records])
        else:
            self.matrix = np.zeros((0, embedder.dim), dtype=np.float32)

    def search(self, query: str, k: int = 5) -> list:
        if not self.records:
            return []
        q = self.embedder.encode([query])[0]
        sims = self.matrix @ q  # both L2-normalised -> cosine similarity
        order = np.argsort(-sims)[:k]
        return [Hit(self.records[i], float(sims[i])) for i in order]


class BM25Retriever:
    name = "bm25"

    def __init__(self, store: MemoryStore, tokenize: Callable[[str], list] = default_tokenize):
        from rank_bm25 import BM25Okapi

        self.store = store
        self.tokenize = tokenize
        self.records: List[MemoryRecord] = store.all()
        self.bm25 = BM25Okapi([tokenize(r.text) for r in self.records]) if self.records else None

    def search(self, query: str, k: int = 5) -> list:
        if not self.records:
            return []
        scores = self.bm25.get_scores(self.tokenize(query))
        order = np.argsort(-scores)[:k]
        return [Hit(self.records[i], float(scores[i])) for i in order]


class HybridRetriever:
    name = "hybrid"

    def __init__(self, dense: DenseRetriever, bm25: BM25Retriever,
                 method: str = "rrf", rrf_k: int = 60, alpha: float = 0.5,
                 pool: int = 20, gate: bool = True):
        self.dense = dense
        self.bm25 = bm25
        self.method = method
        self.rrf_k = rrf_k        # RRF damping; larger -> flatter rank weighting
        self.alpha = alpha        # linear fusion weight on the dense score
        self.pool = pool          # candidates pulled from each retriever before fusing
        # gate: drop non-positive hits before fusing. A BM25 score of 0 means no
        # shared terms — without gating, RRF rewards it just for filling the pool,
        # which can drag a strong dense result *down*. Notebook 08 ablates this.
        self.gate = gate

    def search(self, query: str, k: int = 5) -> list:
        pool = max(self.pool, k)
        dense_hits = self.dense.search(query, pool)
        bm25_hits = self.bm25.search(query, pool)
        if self.gate:
            dense_hits = [h for h in dense_hits if h.score > 0]
            bm25_hits = [h for h in bm25_hits if h.score > 0]
        records = {h.id: h.record for h in (*dense_hits, *bm25_hits)}

        if self.method == "rrf":
            scores = self._rrf(dense_hits, bm25_hits)
        else:
            scores = self._linear(dense_hits, bm25_hits)

        order = sorted(scores, key=lambda i: -scores[i])[:k]
        return [Hit(records[i], scores[i]) for i in order]

    def _rrf(self, dense_hits, bm25_hits) -> dict:
        scores: dict = {}
        for hits in (dense_hits, bm25_hits):
            for rank, hit in enumerate(hits):
                scores[hit.id] = scores.get(hit.id, 0.0) + 1.0 / (self.rrf_k + rank + 1)
        return scores

    def _linear(self, dense_hits, bm25_hits) -> dict:
        def minmax(hits):
            if not hits:
                return {}
            vals = [h.score for h in hits]
            lo, hi = min(vals), max(vals)
            span = (hi - lo) or 1.0
            return {h.id: (h.score - lo) / span for h in hits}

        nd, nb = minmax(dense_hits), minmax(bm25_hits)
        scores: dict = {}
        for hit_id, value in nd.items():
            scores[hit_id] = scores.get(hit_id, 0.0) + self.alpha * value
        for hit_id, value in nb.items():
            scores[hit_id] = scores.get(hit_id, 0.0) + (1.0 - self.alpha) * value
        return scores
