"""A small, hand-labeled memory corpus + retrieval probes (Notebook 08).

The corpus is a developer's personal notes — semantic facts, preferences, dated
episodes, and two *confusable clusters* of near-identical episodic memories that
differ only by an opaque ID (incidents, customer tickets). The probes are split
by ``kind`` to expose the central tradeoff:

* ``paraphrase`` — semantic match, almost no shared words        -> dense wins.
* ``exact-term`` — disambiguate near-identical memories by an ID -> BM25 wins.
* ``mixed``      — semantic intent plus a distinctive term        -> hybrid wins.

The confusable clusters are the realistic case where a strong embedder fails:
the memories are semantically identical, so only the exact token separates them.

Self-contained and deterministic, so retrieval quality is reproducible.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Probe:
    query: str
    relevant_ids: frozenset
    kind: str  # paraphrase | exact-term | mixed


# (id, text, kind) — kind is the *memory* type (semantic/episodic/procedural).
SAMPLE_MEMORIES: list[tuple] = [
    ("m01", "The user prefers dark mode in every editor and terminal.", "semantic"),
    ("m02", "For systems programming the user's language of choice is Rust.", "semantic"),
    ("m03", "On 2026-03-02 the user deployed the billing service to production.", "episodic"),
    ("m04", "The staging database password lives in the vault under key DB_STAGING_PW.", "semantic"),
    ("m05", "Build error E1042 means a missing semicolon in the parser grammar.", "semantic"),
    ("m06", "The user is allergic to peanuts and avoids them when ordering lunch.", "semantic"),
    ("m07", "Project Aurora must keep p99 latency under 200 ms for the search API.", "semantic"),
    ("m08", "On 2026-05-14 the team migrated the inventory service from REST to gRPC.", "episodic"),
    ("m09", "The user dislikes meetings before 10am and prefers async standups.", "semantic"),
    ("m10", "The CI pipeline runs on the self-hosted runner pool named midnight-blue.", "semantic"),
    ("m11", "To rotate the API token run `make rotate-token` and update the .env file.", "procedural"),
    ("m12", "The user lives in Karachi and works in the UTC+5 timezone.", "semantic"),
    ("m13", "Customer ACME-7781 reported intermittent 504 errors during checkout.", "episodic"),
    ("m14", "The lab's default embedding model is all-MiniLM-L6-v2.", "semantic"),
    ("m15", "On 2026-01-09 the user upgraded the cluster to Kubernetes v1.29.", "episodic"),
    ("m16", "The user takes their coffee black, with no sugar.", "semantic"),
    ("m17", "The feature flag beta_search_ranking is enabled for 5% of users.", "semantic"),
    ("m18", "Quarterly planning happens in the first week of each quarter.", "semantic"),
    ("m19", "The user's laptop is a MacBook with an M2 chip and 32 GB of unified memory.", "semantic"),
    ("m20", "Incident INC-2055 was caused by a memory leak in the websocket handler.", "episodic"),
    ("m21", "The design doc for context compression lives in the memory-research repo.", "semantic"),
    ("m22", "The user prefers tabs over spaces, configured to a width of four.", "semantic"),
    ("m23", "On 2026-06-01 the user started building a local LLM research lab.", "episodic"),
    ("m24", "The fallback model for offline tests is SmolLM2-135M-Instruct.", "semantic"),
    # Confusable cluster A — incidents, identical text except the opaque code.
    ("m25", "Incident INC-3071 was caused by a memory leak in the websocket handler.", "episodic"),
    ("m26", "Incident INC-4188 was caused by a memory leak in the websocket handler.", "episodic"),
    ("m27", "Incident INC-5219 was caused by a memory leak in the websocket handler.", "episodic"),
    ("m28", "Incident INC-6634 was caused by a memory leak in the websocket handler.", "episodic"),
    # Confusable cluster B — customer tickets, identical text except the opaque code.
    ("m29", "Customer ACME-3322 reported intermittent 504 errors during checkout.", "episodic"),
    ("m30", "Customer ACME-9090 reported intermittent 504 errors during checkout.", "episodic"),
    ("m31", "Customer ACME-1207 reported intermittent 504 errors during checkout.", "episodic"),
    ("m32", "Customer ACME-5560 reported intermittent 504 errors during checkout.", "episodic"),
]


RETRIEVAL_PROBES: list[Probe] = [
    # paraphrase: semantic intent, lexically disjoint from the target memory
    Probe("How do I like my morning beverage prepared?", frozenset({"m16"}), "paraphrase"),
    Probe("Which colour theme should my tools use?", frozenset({"m01"}), "paraphrase"),
    Probe("What food should I never be served at lunch?", frozenset({"m06"}), "paraphrase"),
    Probe("What computer am I running this lab on?", frozenset({"m19"}), "paraphrase"),
    Probe("When do I like to hold the daily team sync?", frozenset({"m09"}), "paraphrase"),
    Probe("Where in the world am I based?", frozenset({"m12"}), "paraphrase"),
    # exact-term: disambiguate a near-identical memory by its opaque ID
    Probe("Which incident was INC-2055?", frozenset({"m20"}), "exact-term"),
    Probe("Which incident was INC-6634?", frozenset({"m28"}), "exact-term"),
    Probe("Which incident was INC-4188?", frozenset({"m26"}), "exact-term"),
    Probe("What did customer ACME-7781 report?", frozenset({"m13"}), "exact-term"),
    Probe("What did customer ACME-5560 report?", frozenset({"m32"}), "exact-term"),
    Probe("What did customer ACME-9090 report?", frozenset({"m30"}), "exact-term"),
    # mixed: semantic question that also contains a distinctive term
    Probe("What latency target does Project Aurora have?", frozenset({"m07"}), "mixed"),
    Probe("How do I change the API token?", frozenset({"m11"}), "mixed"),
    Probe("Which Kubernetes version is the cluster running?", frozenset({"m15"}), "mixed"),
    Probe("Is the beta_search_ranking flag on?", frozenset({"m17"}), "mixed"),
]


def build_sample_store():
    """A MemoryStore preloaded with SAMPLE_MEMORIES."""
    from llmlab.memory.store import MemoryStore

    store = MemoryStore()
    store.add_many(SAMPLE_MEMORIES)
    return store
