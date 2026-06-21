"""Retrieval quality metrics — make 'memory recall' a measured variable (NB 08).

``recall@k``  — fraction of the gold-relevant memories found in the top *k*.
``MRR@k``     — mean reciprocal rank of the *first* relevant memory (rank matters,
                not just presence).

``evaluate_retriever`` runs any retriever over a set of ``Probe``s and reports
both, with a per-category breakdown so the dense/lexical/hybrid story is legible.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Sequence


def recall_at_k(retrieved_ids: Sequence[str], relevant_ids, k: int) -> float:
    relevant = set(relevant_ids)
    if not relevant:
        return 0.0
    topk = set(list(retrieved_ids)[:k])
    return len(relevant & topk) / len(relevant)


def mrr_at_k(retrieved_ids: Sequence[str], relevant_ids, k: int) -> float:
    relevant = set(relevant_ids)
    for rank, hit_id in enumerate(list(retrieved_ids)[:k], start=1):
        if hit_id in relevant:
            return 1.0 / rank
    return 0.0


@dataclass
class RetrievalReport:
    name: str
    k: int
    recall_at_k: float
    mrr: float
    n: int
    per_probe: list = field(default_factory=list)

    def recall_by_category(self) -> dict:
        buckets = defaultdict(list)
        for row in self.per_probe:
            buckets[row["kind"]].append(row["recall"])
        return {kind: sum(vals) / len(vals) for kind, vals in buckets.items()}


def evaluate_retriever(retriever, probes, k: int = 3) -> RetrievalReport:
    rows = []
    for probe in probes:
        hits = retriever.search(probe.query, k)
        retrieved = [h.id for h in hits]
        rows.append({
            "query": probe.query,
            "kind": probe.kind,
            "relevant": set(probe.relevant_ids),
            "retrieved": retrieved,
            "recall": recall_at_k(retrieved, probe.relevant_ids, k),
            "rr": mrr_at_k(retrieved, probe.relevant_ids, k),
        })
    n = len(rows) or 1
    return RetrievalReport(
        name=getattr(retriever, "name", "retriever"),
        k=k,
        recall_at_k=sum(r["recall"] for r in rows) / n,
        mrr=sum(r["rr"] for r in rows) / n,
        n=len(rows),
        per_probe=rows,
    )
