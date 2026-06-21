"""A tiny, transparent memory store (Notebook 08).

A ``MemoryStore`` is just an ordered collection of ``MemoryRecord``s — text plus
light metadata (a ``kind`` and a timestamp, which later notebooks use for
recency/forgetting policies). Retrieval is deliberately *not* a method here: it
lives in ``llmlab/retrieval`` so dense, lexical, and hybrid backends can be
swapped and compared over the same store.
"""
from __future__ import annotations

import itertools
import json
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable, Optional, Union


@dataclass
class MemoryRecord:
    id: str
    text: str
    kind: str = "semantic"          # e.g. semantic | episodic | procedural
    metadata: dict = field(default_factory=dict)
    ts: float = field(default_factory=time.time)


# An item to add: a raw string, a (id, text) / (id, text, kind) tuple, a dict, or a record.
AddItem = Union[str, tuple, dict, MemoryRecord]


class MemoryStore:
    def __init__(self):
        self._records: dict[str, MemoryRecord] = {}
        self._counter = itertools.count(1)

    def add(self, text: str, *, id: Optional[str] = None, kind: str = "semantic",
            metadata: Optional[dict] = None, ts: Optional[float] = None) -> MemoryRecord:
        if id is None:
            id = f"m{next(self._counter):03d}"
        if id in self._records:
            raise ValueError(f"duplicate memory id: {id!r}")
        record = MemoryRecord(
            id=id, text=text, kind=kind,
            metadata=dict(metadata or {}),
            ts=time.time() if ts is None else ts,
        )
        self._records[id] = record
        return record

    def add_many(self, items: Iterable[AddItem]) -> list:
        added = []
        for item in items:
            if isinstance(item, MemoryRecord):
                if item.id in self._records:
                    raise ValueError(f"duplicate memory id: {item.id!r}")
                self._records[item.id] = item
                added.append(item)
            elif isinstance(item, str):
                added.append(self.add(item))
            elif isinstance(item, dict):
                added.append(self.add(**item))
            else:  # tuple: (id, text) or (id, text, kind)
                id_, text_, *rest = item
                added.append(self.add(text_, id=id_, kind=rest[0] if rest else "semantic"))
        return added

    def get(self, id: str) -> MemoryRecord:
        return self._records[id]

    def remove(self, id: str) -> MemoryRecord:
        """Drop a memory (used by forgetting / capacity policies)."""
        return self._records.pop(id)

    def all(self) -> list:
        return list(self._records.values())

    def ids(self) -> list:
        return list(self._records)

    def texts(self) -> list:
        return [r.text for r in self._records.values()]

    def __len__(self) -> int:
        return len(self._records)

    def __iter__(self):
        return iter(self._records.values())

    # --- persistence (embeddings are recomputed by the retriever on load) ---
    def save_jsonl(self, path: Union[str, Path]) -> Path:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w") as fh:
            for record in self._records.values():
                fh.write(json.dumps(asdict(record)) + "\n")
        return path

    @classmethod
    def load_jsonl(cls, path: Union[str, Path]) -> "MemoryStore":
        store = cls()
        for line in Path(path).read_text().splitlines():
            if line.strip():
                store.add_many([json.loads(line)])
        return store
