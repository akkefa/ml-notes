Large Language Models
=====================

A local-first LLM research lab for studying inference internals, agents built
from scratch, and - above all - **memory and context-window limitations** on
Apple Silicon (M2, 32 GB).

This section uses its own virtual environment, kept separate from the docs
build so model downloads never run on Read the Docs::

   uv venv --python 3.11 .venv-llm
   source .venv-llm/bin/activate
   uv pip install -r llm-requirements.txt

.. toctree::
   :maxdepth: 1

   notebooks/00_environment_check
   notebooks/01_tokenizers_and_chat_templates
   notebooks/02_local_inference_transformers
   notebooks/05_attention_and_kv_cache
   notebooks/06_prompted_reasoning
   notebooks/07_manual_tool_calling_agent
   notebooks/08_memory_store_basics
   notebooks/09_retrieval_augmented_agent
   notebooks/10_memory_evaluation_harness
