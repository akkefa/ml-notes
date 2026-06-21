# Local LLM Research Lab (`docs/LLM/`)

A local-first lab for understanding large language models by building from
scratch on Apple Silicon (M2, 32 GB). Focus areas: inference internals, a
hand-written agent loop, and **memory / context-window research**.

## Setup

This lab uses its own virtual environment, separate from the docs build:

```bash
uv venv --python 3.11 .venv-llm
source .venv-llm/bin/activate
uv pip install -r llm-requirements.txt
```

Model downloads are cached in the repo-local `.hf_cache/` (git-ignored).

## Layout

- `notebooks/` — guided experiment sequence (`00_...` -> `15_...`)
- `llmlab/` — reusable, tested Python package (models, agent, memory, retrieval, evals)
- `tests/` — pytest suite
- `data/`, `stores/`, `models/`, `runs/` — generated artifacts (git-ignored)
- `results/` — small committed metrics + figures

## Run the smoke test

```bash
source .venv-llm/bin/activate
jupyter nbconvert --to notebook --execute --inplace docs/LLM/notebooks/00_environment_check.ipynb
pytest docs/LLM/tests -m "not slow"
```

> Notebooks under `docs/LLM/notebooks/` are excluded from the Sphinx/RTD build
> execution (see `nb_execution_excludepatterns` in `docs/conf.py`); their stored
> outputs are what render on the site.
