"""Tests for tokenizer inspection + manual chat-template rendering (Notebook 01).

Pure-string renderer tests are fast (no downloads). The ``slow``-marked tests
assert byte-for-byte equality against the *real* tokenizers and need network on
first run.
"""
from __future__ import annotations

import pytest

from llmlab.tokenization import (
    QWEN_DEFAULT_SYSTEM,
    SMOLLM2_DEFAULT_SYSTEM,
    first_diff,
    render_chatml,
    render_llama3,
    render_mistral_inst,
)

USER = [{"role": "user", "content": "Hello, who are you?"}]
SYS_USER = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hi"},
]


# --- pure string renderers (fast, offline) ---------------------------------
def test_render_chatml_injects_default_system():
    assert render_chatml(USER, default_system=SMOLLM2_DEFAULT_SYSTEM) == (
        "<|im_start|>system\n"
        "You are a helpful AI assistant named SmolLM, trained by Hugging Face<|im_end|>\n"
        "<|im_start|>user\nHello, who are you?<|im_end|>\n"
        "<|im_start|>assistant\n"
    )


def test_render_chatml_keeps_explicit_system():
    assert render_chatml(SYS_USER, default_system=QWEN_DEFAULT_SYSTEM) == (
        "<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n"
        "<|im_start|>user\nHi<|im_end|>\n"
        "<|im_start|>assistant\n"
    )


def test_render_llama3_user_only():
    assert render_llama3(USER) == (
        "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n"
        "Hello, who are you?<|eot_id|>"
        "<|start_header_id|>assistant<|end_header_id|>\n\n"
    )


def test_render_mistral_user_only():
    assert render_mistral_inst(USER) == "<s>[INST] Hello, who are you?[/INST]"


def test_render_mistral_merges_system_into_user():
    assert render_mistral_inst(SYS_USER) == "<s>[INST] You are a helpful assistant.\n\nHi[/INST]"


def test_first_diff_reports_identical():
    assert first_diff("abc", "abc") == "identical"


def test_first_diff_reports_index():
    assert "index 2" in first_diff("abXd", "abYd")


# --- integration vs the real tokenizers (slow, needs download) -------------
@pytest.mark.slow
@pytest.mark.parametrize(
    "model_id,default_system",
    [
        ("HuggingFaceTB/SmolLM2-135M-Instruct", SMOLLM2_DEFAULT_SYSTEM),
        ("Qwen/Qwen2.5-0.5B-Instruct", QWEN_DEFAULT_SYSTEM),
    ],
)
def test_chatml_matches_official(model_id, default_system):
    from llmlab.tokenization import load_tokenizer

    tok = load_tokenizer(model_id)
    official = tok.apply_chat_template(USER, tokenize=False, add_generation_prompt=True)
    assert render_chatml(USER, default_system=default_system) == official


@pytest.mark.slow
def test_llama3_matches_official():
    from llmlab.tokenization import load_tokenizer

    tok = load_tokenizer("NousResearch/Meta-Llama-3-8B-Instruct")
    official = tok.apply_chat_template(SYS_USER, tokenize=False, add_generation_prompt=True)
    assert render_llama3(SYS_USER) == official


@pytest.mark.slow
def test_mistral_matches_official():
    from llmlab.tokenization import load_tokenizer

    tok = load_tokenizer("mistralai/Mistral-7B-Instruct-v0.3")
    official = tok.apply_chat_template(SYS_USER, tokenize=False)
    assert render_mistral_inst(SYS_USER) == official
