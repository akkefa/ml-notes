"""Central configuration for the local LLM research lab.

All paths are resolved relative to this file, so notebooks and tests can call
``from llmlab import config`` regardless of the current working directory.

Generated artifacts (datasets, vector stores, weights, run logs) are written
under ``docs/LLM/`` into git-ignored directories. Model downloads are routed to
the repo-local ``.hf_cache/`` so nothing lands in your home directory.
"""
from __future__ import annotations

import os
import random
from pathlib import Path

# --- Paths -----------------------------------------------------------------
LLM_DIR = Path(__file__).resolve().parents[1]   # docs/LLM
DOCS_DIR = LLM_DIR.parent                        # docs
REPO_ROOT = DOCS_DIR.parent                      # repository root

DATA_DIR = LLM_DIR / "data"
STORES_DIR = LLM_DIR / "stores"
MODELS_DIR = LLM_DIR / "models"
RUNS_DIR = LLM_DIR / "runs"
RESULTS_DIR = LLM_DIR / "results"

HF_CACHE_DIR = REPO_ROOT / ".hf_cache"
MPL_CACHE_DIR = REPO_ROOT / ".mpl_cache"

_ARTIFACT_DIRS = (DATA_DIR, STORES_DIR, MODELS_DIR, RUNS_DIR, RESULTS_DIR)


# --- Environment -----------------------------------------------------------
def configure_caches() -> None:
    """Route Hugging Face + matplotlib caches to repo-local, git-ignored dirs."""
    HF_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    MPL_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("HF_HOME", str(HF_CACHE_DIR))
    os.environ.setdefault("MPLCONFIGDIR", str(MPL_CACHE_DIR))
    # Quiet a noisy fork-related warning when tokenizers are used in notebooks.
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")


def ensure_dirs() -> None:
    """Create the git-ignored artifact directories if they do not exist."""
    for directory in _ARTIFACT_DIRS:
        directory.mkdir(parents=True, exist_ok=True)


def get_device(prefer_mps: bool = True) -> str:
    """Return the best available torch device: ``mps`` > ``cuda`` > ``cpu``."""
    try:
        import torch
    except ImportError:
        return "cpu"
    if prefer_mps and torch.backends.mps.is_available():
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


def seed_everything(seed: int = 42) -> int:
    """Seed Python, NumPy, torch (incl. MPS) and MLX for reproducible runs."""
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    try:
        import numpy as np

        np.random.seed(seed)
    except ImportError:
        pass
    try:
        import torch

        torch.manual_seed(seed)
        if torch.backends.mps.is_available():
            torch.mps.manual_seed(seed)
    except ImportError:
        pass
    try:
        import mlx.core as mx

        mx.random.seed(seed)
    except Exception:
        # MLX may be installed but unable to load a Metal device (headless / CI /
        # sandboxed sessions). Seeding it is best-effort, so never fail here.
        pass
    return seed
