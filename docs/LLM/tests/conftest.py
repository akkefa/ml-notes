"""Pytest fixtures for the LLM lab. Keeps the model tiny so tests stay fast."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

# Make ``llmlab`` importable without installing the package (docs/LLM on path).
LLM_DIR = Path(__file__).resolve().parents[1]
if str(LLM_DIR) not in sys.path:
    sys.path.insert(0, str(LLM_DIR))

TINY_MODEL_ID = "HuggingFaceTB/SmolLM2-135M-Instruct"


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "slow: marks tests that download/load models (deselect with -m 'not slow')",
    )


@pytest.fixture(scope="session")
def tiny_model():
    """Load SmolLM2-135M-Instruct once per test session."""
    from llmlab import config as llm_config

    llm_config.configure_caches()
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(TINY_MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(TINY_MODEL_ID).to(llm_config.get_device())
    model.eval()
    return tokenizer, model
