"""Writing to memory — *what* to store and *when* (Notebook 10).

Retrieval (NB 08) and grounding (NB 09) are the read side. This is the write
side, and it is where the interesting policy choices live:

* **write-all** — store every fact verbatim (the baseline).
* **dedup** — skip a fact that is near-identical to one already stored
  (cosine >= ``dedup_threshold``). Shrinks the store — but, as Notebook 10
  shows, an aggressive threshold *merges away* the confusable clusters whose
  whole point is a distinguishing ID.
* **capacity** — a bounded store that evicts the oldest memory (forgetting).

The writer keeps its own embedding matrix so dedup is a single matrix-vector
product, with no re-embedding of the store.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np

from llmlab.memory.store import MemoryRecord, MemoryStore


@dataclass
class WriteResult:
    stored: bool
    record: Optional[MemoryRecord]
    reason: str                       # "stored" | "duplicate"
    merged_into: Optional[str] = None
    evicted: Optional[str] = None


class MemoryWriter:
    def __init__(self, store: MemoryStore, embedder,
                 dedup_threshold: Optional[float] = None, capacity: Optional[int] = None):
        self.store = store
        self.embedder = embedder
        self.dedup_threshold = dedup_threshold
        self.capacity = capacity
        self._ids: list = []          # writer-added ids, oldest first
        self._emb: Optional[np.ndarray] = None  # (n, d), aligned with _ids

    def write(self, text: str, *, kind: str = "episodic", **metadata) -> WriteResult:
        vec = self.embedder.encode([text])[0]

        if self.dedup_threshold is not None and self._emb is not None and len(self._ids):
            sims = self._emb @ vec
            j = int(np.argmax(sims))
            if float(sims[j]) >= self.dedup_threshold:
                return WriteResult(False, self.store.get(self._ids[j]), "duplicate",
                                   merged_into=self._ids[j])

        record = self.store.add(text, kind=kind, metadata=metadata)
        self._ids.append(record.id)
        self._emb = vec[None, :] if self._emb is None else np.vstack([self._emb, vec])

        evicted = None
        if self.capacity is not None and len(self._ids) > self.capacity:
            evicted = self._evict_oldest()
        return WriteResult(True, record, "stored", evicted=evicted)

    def _evict_oldest(self) -> str:
        old_id = self._ids.pop(0)
        self._emb = self._emb[1:]
        self.store.remove(old_id)
        return old_id
