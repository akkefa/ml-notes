"""Text embedders for dense retrieval (Notebook 08).

``Embedder`` wraps a sentence-transformers model (default
``all-MiniLM-L6-v2``: 384-dim, ~80 MB, fast on MPS). ``HashingEmbedder`` is a
deterministic, dependency-free bag-of-hashed-tokens fallback used by the test
suite so retrieval *mechanics* can be tested without any model download.
"""
from __future__ import annotations

import hashlib
import re
from typing import Optional, Sequence

import numpy as np

_TOKEN_RE = re.compile(r"[a-z0-9]+")
DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


class Embedder:
    """Lazy sentence-transformers wrapper returning L2-normalised float32 vectors."""

    def __init__(self, model_id: str = DEFAULT_MODEL, device: Optional[str] = None):
        self.model_id = model_id
        self.device = device
        self._model = None

    def _ensure(self):
        if self._model is None:
            from sentence_transformers import SentenceTransformer

            self._model = SentenceTransformer(self.model_id, device=self.device)
        return self._model

    @property
    def dim(self) -> int:
        model = self._ensure()
        # sentence-transformers renamed this getter; support both spellings.
        getter = getattr(model, "get_embedding_dimension", None) or model.get_sentence_embedding_dimension
        return getter()

    def encode(self, texts: Sequence[str], normalize: bool = True, batch_size: int = 32) -> np.ndarray:
        model = self._ensure()
        emb = model.encode(
            list(texts),
            normalize_embeddings=normalize,
            batch_size=batch_size,
            convert_to_numpy=True,
            show_progress_bar=False,
        )
        return np.asarray(emb, dtype=np.float32)


class HashingEmbedder:
    """Deterministic bag-of-hashed-tokens vectors — no model, for tests/offline.

    Captures lexical overlap (shared tokens -> higher cosine), *not* semantics,
    so it is only useful for exercising the retrieval plumbing.
    """

    def __init__(self, dim: int = 256, seed: int = 0):
        self._dim = dim
        self.seed = seed

    @property
    def dim(self) -> int:
        return self._dim

    def _vec(self, text: str) -> np.ndarray:
        vec = np.zeros(self._dim, dtype=np.float32)
        for token in _TOKEN_RE.findall(text.lower()):
            digest = hashlib.md5(f"{self.seed}:{token}".encode()).hexdigest()
            vec[int(digest, 16) % self._dim] += 1.0
        return vec

    def encode(self, texts: Sequence[str], normalize: bool = True, **_) -> np.ndarray:
        texts = list(texts)
        if not texts:
            return np.zeros((0, self._dim), dtype=np.float32)
        mat = np.stack([self._vec(t) for t in texts])
        if normalize:
            norms = np.linalg.norm(mat, axis=1, keepdims=True)
            norms[norms == 0] = 1.0
            mat = mat / norms
        return mat
