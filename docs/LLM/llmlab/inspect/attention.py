"""Quantifying attention structure (Notebook 05).

All helpers take the ``outputs.attentions`` tuple from a forward pass run with
``attn_implementation="eager", output_attentions=True``: one tensor per layer of
shape ``(batch, heads, query, key)``. Unless noted they summarise the **last
query token** (the position that predicts the next token), averaged over heads.
"""
from __future__ import annotations

from typing import Sequence


def attention_to_first_token(attentions: Sequence) -> list:
    """Per-layer fraction of attention the last query places on token 0.

    Large values are the *attention sink* (Xiao et al., StreamingLLM): models
    dump probability mass onto the first token as a no-op. It is why naive KV
    eviction that drops early tokens wrecks quality — and a key constraint for
    cache-compression research.
    """
    vals = []
    for layer_attn in attentions:
        last_query = layer_attn[0, :, -1, :]  # (heads, key)
        vals.append(float(last_query[:, 0].mean()))
    return vals


def attention_entropy(attentions: Sequence) -> list:
    """Per-layer mean entropy (nats) of the last query's attention.

    Low entropy = sharply focused on a few tokens; high entropy = diffuse.
    """
    import torch

    out = []
    for layer_attn in attentions:
        p = layer_attn[0, :, -1, :].clamp_min(1e-12)  # (heads, key)
        ent = -(p * p.log()).sum(-1)  # (heads,)
        out.append(float(ent.mean()))
    return out


def mean_attention_distance(attentions: Sequence) -> list:
    """Per-layer mean distance (in tokens) between the last query and its keys.

    Small = local/recency attention; large = long-range. Lets us see which
    layers actually use far-away context.
    """
    import torch

    out = []
    for layer_attn in attentions:
        p = layer_attn[0, :, -1, :]  # (heads, key)
        key_len = p.shape[-1]
        positions = torch.arange(key_len, device=p.device, dtype=p.dtype)
        distance = (key_len - 1) - positions  # query sits at key_len - 1
        mean_dist = (p * distance).sum(-1)  # (heads,)
        out.append(float(mean_dist.mean()))
    return out


def head_attention_to_first_token(attentions: Sequence):
    """``(n_layers, n_heads)`` tensor of last-query attention onto token 0.

    Useful for spotting that *specific* heads, not whole layers, are the sinks.
    """
    import torch

    rows = [layer_attn[0, :, -1, 0] for layer_attn in attentions]  # each (heads,)
    return torch.stack(rows, dim=0).float().cpu()
