"""Tests for the inference-internals toolkit (Notebook 05).

Fast tests cover the pure functions (KV formula, recall scoring) and the
haystack builder against a *cached* tokenizer loaded in offline mode. Model-
backed tests are marked ``slow`` and reuse tiny SmolLM2-135M.
"""
from __future__ import annotations

import pytest

from llmlab.inspect.longcontext import (
    QUESTION,
    make_haystack,
    passkey_messages,
    recall_hit,
)
from llmlab.inspect.profiling import kv_cache_bytes

TINY = "HuggingFaceTB/SmolLM2-135M-Instruct"


# --- fast, pure functions --------------------------------------------------
def test_kv_cache_bytes_matches_nb02_per_token():
    # 24 layers, 2 KV heads, head_dim 64, fp32 -> 24576 bytes/token (Qwen2.5-0.5B)
    assert kv_cache_bytes(24, 2, 64, 1, dtype_bytes=4) == 24576


def test_kv_cache_bytes_scales_linearly_in_length():
    base = kv_cache_bytes(12, 4, 64, 100, dtype_bytes=2)
    assert kv_cache_bytes(12, 4, 64, 1000, dtype_bytes=2) == 10 * base


def test_recall_hit_requires_standalone_number():
    assert recall_hit("The passkey is 48291.", 48291) is True
    assert recall_hit("48291", 48291) is True
    assert recall_hit("It might be 4829", 48291) is False  # substring must not count
    assert recall_hit("no idea", 48291) is False


# --- cached tokenizer (no model weights) -----------------------------------
@pytest.fixture(scope="module")
def tok():
    from llmlab import config

    config.configure_caches()  # route HF_HOME before transformers is imported
    from transformers import AutoTokenizer

    return AutoTokenizer.from_pretrained(TINY)


@pytest.mark.slow
def test_make_haystack_grows_and_keeps_needle(tok):
    short = make_haystack(tok, 50, " NEEDLEWORD ", depth=0.5)
    long = make_haystack(tok, 600, " NEEDLEWORD ", depth=0.5)
    assert len(long) > len(short)
    assert "NEEDLEWORD" in short


@pytest.mark.slow
def test_passkey_messages_embeds_passkey_and_question(tok):
    messages = passkey_messages(tok, 12345, n_tokens=120, depth=0.3)
    assert messages[0]["role"] == "user"
    assert "12345" in messages[0]["content"]
    assert QUESTION in messages[0]["content"]


@pytest.mark.slow
def test_multikey_messages_plants_indexed_keys(tok):
    from llmlab.inspect.longcontext import multikey_messages

    messages = multikey_messages(tok, 200, [11111, 22222, 33333], query_index=1)
    content = messages[0]["content"]
    assert "Passkey number 2 is 22222" in content  # planted verbatim
    assert "passkey number 2?" in content  # the question targets index 2 (1-based)


# --- slow, model-backed ----------------------------------------------------
@pytest.fixture(scope="module")
def lm():
    from llmlab import config
    from llmlab.models.local_model import LocalModel

    config.configure_caches()
    return LocalModel(TINY)


@pytest.mark.slow
def test_context_scaling_grows_with_length(lm):
    from llmlab.inspect.profiling import context_scaling

    points = context_scaling(lm.model, [32, 64], n_decode=2)
    assert len(points) == 2
    assert points[1].kv_mib > points[0].kv_mib
    assert points[0].prefill_s > 0 and points[0].decode_s_per_tok > 0


@pytest.mark.slow
def test_attention_helpers_shapes_and_ranges(lm):
    from llmlab.inspect import attention as attn

    _, outputs = lm.forward(
        [{"role": "user", "content": "Hello there, friend."}], output_attentions=True
    )
    n_layers = lm.model.config.num_hidden_layers
    sink = attn.attention_to_first_token(outputs.attentions)
    entropy = attn.attention_entropy(outputs.attentions)
    distance = attn.mean_attention_distance(outputs.attentions)
    assert len(sink) == n_layers == len(entropy) == len(distance)
    assert all(0.0 <= s <= 1.0001 for s in sink)
    mat = attn.head_attention_to_first_token(outputs.attentions)
    assert mat.shape[0] == n_layers


@pytest.mark.slow
def test_passkey_grid_structure(lm):
    from llmlab.inspect.longcontext import run_passkey_grid

    results = run_passkey_grid(lm, lengths=[64], depths=[0.5], max_new_tokens=6)
    assert len(results) == 1
    assert isinstance(results[0].hit, bool)
    assert results[0].prompt_tokens > 50


@pytest.mark.slow
def test_multikey_grid_queries_every_key(lm):
    from llmlab.inspect.longcontext import run_multikey_grid

    results = run_multikey_grid(lm, lengths=[128], n_keys=3, max_new_tokens=6, seed=1)
    assert len(results) == 3
    assert {r.query_index for r in results} == {0, 1, 2}
    assert all(isinstance(r.hit, bool) for r in results)
