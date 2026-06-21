"""Smoke tests for the lab environment (Task 00)."""
from __future__ import annotations

import os

import pytest

from llmlab import config


def test_get_device_is_valid():
    assert config.get_device() in {"mps", "cuda", "cpu"}


def test_ensure_dirs_creates_results():
    config.ensure_dirs()
    assert config.RESULTS_DIR.is_dir()


def test_seed_everything_returns_seed():
    assert config.seed_everything(123) == 123


def test_configure_caches_sets_hf_home(monkeypatch):
    monkeypatch.delenv("HF_HOME", raising=False)
    config.configure_caches()
    assert os.environ["HF_HOME"] == str(config.HF_CACHE_DIR)


@pytest.mark.slow
def test_tiny_model_generates(tiny_model):
    tokenizer, model = tiny_model
    messages = [{"role": "user", "content": "Say hello in three words."}]
    inputs = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_tensors="pt", return_dict=True
    ).to(model.device)
    prompt_len = inputs["input_ids"].shape[-1]
    output = model.generate(**inputs, max_new_tokens=8, do_sample=False)
    text = tokenizer.decode(output[0, prompt_len:], skip_special_tokens=True)
    assert isinstance(text, str) and len(text.strip()) > 0
