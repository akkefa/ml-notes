"""A ``retrieve`` tool that bridges the agent (NB 07) to the memory store (NB 08).

This is the read side of agentic memory: the agent emits a query, the tool runs
a retriever over the store, and the top hits come back as a numbered observation
the model can read. Registering it next to ``final_answer`` gives a minimal
retrieval-augmented agent (Notebook 09).
"""
from __future__ import annotations

from llmlab.agent.tools import FINAL_ANSWER, Tool, ToolRegistry


def format_hits(hits) -> str:
    """Render retriever hits as a numbered, ID-tagged observation."""
    if not hits:
        return "No memories found for that query."
    return "\n".join(f"[{i}] ({h.id}) {h.text}" for i, h in enumerate(hits, start=1))


def make_retrieve_tool(retriever, k: int = 3, min_score=None, followup: str = "") -> Tool:
    """A retrieve tool. ``followup`` is appended to every observation — a place to
    remind a small model to *decide* (answer or abstain) instead of re-searching."""
    def run(args: dict) -> str:
        query = args.get("query")
        if not query:
            return "Error: retrieve needs a 'query' string argument."
        hits = retriever.search(str(query), k)
        if min_score is not None:
            hits = [h for h in hits if h.score >= min_score]
        observation = format_hits(hits)
        return f"{observation}\n{followup}" if followup else observation

    return Tool(
        name="retrieve",
        description="search long-term memory and return the most relevant notes.",
        run=run,
        args_hint='{"query": "<what to look up>"}',
    )


def make_memory_registry(retriever, k: int = 3, min_score=None, followup: str = "") -> ToolRegistry:
    """A ``retrieve`` tool plus a text-valued ``final_answer``."""
    registry = ToolRegistry()
    registry.register(make_retrieve_tool(retriever, k=k, min_score=min_score, followup=followup))
    registry.register(Tool(
        name=FINAL_ANSWER,
        description="give your final answer and stop.",
        run=lambda args: str(args.get("answer", "")),
        args_hint='{"answer": "<your answer, or \'I don\'t know\'>"}',
    ))
    return registry
