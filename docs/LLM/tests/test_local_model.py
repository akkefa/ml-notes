"""Tests for the Hugging Face inference backend (Notebook 02).

The headline test is the *equivalence*: a hand-written greedy loop must match
``model.generate`` token-for-token. Model-loading tests are marked ``slow``;
they reuse the tiny cached SmolLM2-135M.
"""
from __future__ import annotations

import pytest

from llmlab.models.local_model import GenerationResult, SamplingConfig

TINY = "HuggingFaceTB/SmolLM2-135M-Instruct"
MESSAGES = [{"role": "user", "content": "List three primary colors."}]


# --- fast, offline ---------------------------------------------------------
def test_sampling_config_defaults_to_clean_greedy():
    cfg = SamplingConfig()
    assert cfg.do_sample is False
    assert cfg.repetition_penalty == 1.0


def test_generation_result_fields():
    res = GenerationResult(text="hi", prompt_tokens=3, new_tokens=1, token_ids=[5])
    assert res.text == "hi" and res.new_tokens == 1


# --- slow integration ------------------------------------------------------
@pytest.fixture(scope="module")
def lm():
    from llmlab import config
    from llmlab.models.local_model import LocalModel

    config.configure_caches()
    return LocalModel(TINY)


@pytest.mark.slow
def test_greedy_decode_matches_generate(lm):
    """The success criterion of Notebook 02."""
    import torch

    from llmlab.models.local_model import greedy_decode

    inputs = lm.to_input(MESSAGES)
    with torch.no_grad():
        reference = lm.model.generate(
            **inputs,
            max_new_tokens=30,
            do_sample=False,
            repetition_penalty=1.0,
            num_beams=1,
            pad_token_id=lm.tokenizer.eos_token_id,
        )
    manual = greedy_decode(
        lm.model,
        inputs["input_ids"],
        attention_mask=inputs.get("attention_mask"),
        max_new_tokens=30,
        eos_token_id=lm.tokenizer.eos_token_id,
    )
    assert reference[0].tolist() == manual[0].tolist()


@pytest.mark.slow
def test_generate_returns_text(lm):
    res = lm.generate(MESSAGES, SamplingConfig(max_new_tokens=12))
    assert isinstance(res.text, str) and res.new_tokens > 0


@pytest.mark.slow
def test_forward_exposes_internals(lm):
    inputs, outputs = lm.forward(MESSAGES, output_attentions=True, output_hidden_states=True)
    n_layers = lm.model.config.num_hidden_layers
    assert outputs.logits.shape[0] == 1
    assert len(outputs.hidden_states) == n_layers + 1  # embeddings + each block
    assert len(outputs.attentions) == n_layers
    assert outputs.attentions[0] is not None  # eager attention returns weights
