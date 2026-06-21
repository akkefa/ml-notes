"""KV-cache accounting and context-length scaling measurements (Notebook 05).

The question this module answers: *what does context length actually cost?*

- ``kv_cache_bytes`` — the exact, analytical size of the KV cache.
- ``time_prefill`` / ``time_decode`` — latency of the two distinct phases.
- ``context_scaling`` — sweep prefill length and record latency + memory.

Heavy imports (torch/psutil) are deferred so importing this module stays cheap.
"""
from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Optional, Sequence


def kv_cache_bytes(
    n_layers: int,
    n_kv_heads: int,
    head_dim: int,
    seq_len: int,
    dtype_bytes: int = 2,
) -> int:
    """Exact KV cache size in bytes.

    Two tensors (keys + values), per layer, of shape
    ``(n_kv_heads, seq_len, head_dim)``. Note it uses the number of *key/value*
    heads, not query heads — that is the whole point of GQA/MQA.
    """
    return 2 * n_layers * n_kv_heads * head_dim * seq_len * dtype_bytes


def _sync() -> None:
    import torch

    if torch.backends.mps.is_available():
        torch.mps.synchronize()
    elif torch.cuda.is_available():
        torch.cuda.synchronize()


def mps_allocated_mib() -> float:
    """Currently-allocated MPS memory in MiB (NaN off Apple Silicon)."""
    import torch

    if torch.backends.mps.is_available():
        return torch.mps.current_allocated_memory() / 1024 ** 2
    return float("nan")


def rss_mib() -> float:
    """Resident set size of this process in MiB."""
    import psutil

    return psutil.Process().memory_info().rss / 1024 ** 2


def time_prefill(model, input_ids, attention_mask=None, repeats: int = 3):
    """Best-of-``repeats`` time for a single full forward pass (prefill).

    Returns ``(seconds, outputs)`` where ``outputs`` carries the populated KV
    cache for the prompt.
    """
    import torch

    with torch.no_grad():  # warmup (kernel compilation, allocator)
        outputs = model(input_ids=input_ids, attention_mask=attention_mask, use_cache=True)
    _sync()
    best = float("inf")
    for _ in range(repeats):
        t0 = time.perf_counter()
        with torch.no_grad():
            outputs = model(input_ids=input_ids, attention_mask=attention_mask, use_cache=True)
        _sync()
        best = min(best, time.perf_counter() - t0)
    return best, outputs


def time_decode(model, input_ids, attention_mask=None, n_steps: int = 8) -> float:
    """Average per-token decode latency at the given context length.

    Each step appends one cached token, so this captures how decoding slows as
    the KV cache (and therefore the attention read) grows.
    """
    import torch

    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask, use_cache=True)
    past = outputs.past_key_values
    next_id = outputs.logits[:, -1:, :].argmax(-1)
    mask = attention_mask
    _sync()
    t0 = time.perf_counter()
    with torch.no_grad():
        for _ in range(n_steps):
            if mask is not None:
                mask = torch.cat([mask, torch.ones_like(next_id)], dim=-1)
            outputs = model(
                input_ids=next_id,
                attention_mask=mask,
                past_key_values=past,
                use_cache=True,
            )
            past = outputs.past_key_values
            next_id = outputs.logits[:, -1:, :].argmax(-1)
    _sync()
    return (time.perf_counter() - t0) / n_steps


@dataclass
class ScalePoint:
    seq_len: int
    prefill_s: float
    decode_s_per_tok: float
    kv_mib: float
    mps_alloc_mib: float


def context_scaling(
    model,
    lengths: Sequence[int],
    n_decode: int = 8,
    dtype_bytes: Optional[int] = None,
) -> list:
    """Sweep prefill length and record latency + memory at each point.

    Uses random token ids: content does not affect compute or cache size, so
    this isolates the effect of *length* alone.
    """
    import torch

    cfg = model.config
    n_kv = getattr(cfg, "num_key_value_heads", cfg.num_attention_heads)
    head_dim = getattr(cfg, "head_dim", cfg.hidden_size // cfg.num_attention_heads)
    if dtype_bytes is None:
        dtype_bytes = torch.finfo(next(model.parameters()).dtype).bits // 8
    device = next(model.parameters()).device

    points = []
    for length in lengths:
        if torch.backends.mps.is_available():
            torch.mps.empty_cache()
        ids = torch.randint(0, cfg.vocab_size, (1, length), device=device)
        mask = torch.ones_like(ids)
        prefill_s, _ = time_prefill(model, ids, mask)
        decode_s = time_decode(model, ids, mask, n_steps=n_decode)
        kv_mib = kv_cache_bytes(
            cfg.num_hidden_layers, n_kv, head_dim, length, dtype_bytes
        ) / 1024 ** 2
        points.append(
            ScalePoint(
                seq_len=int(length),
                prefill_s=prefill_s,
                decode_s_per_tok=decode_s,
                kv_mib=kv_mib,
                mps_alloc_mib=mps_allocated_mib(),
            )
        )
    return points
