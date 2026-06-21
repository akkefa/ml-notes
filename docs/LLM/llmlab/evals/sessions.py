"""Multi-turn session benchmark — does memory beat the context window? (NB 10).

Each session states a set of facts (each with a distinctive, verbatim answer)
interleaved with filler chit-chat, then asks about every fact at the end. A
fact's **distance** is how many turns back it was stated. Plotting recall vs
distance is the decisive test: a fixed context window forgets old facts; an
external store should not.

Facts use distinctive tokens (codes, plates, tags) so substring scoring is
robust and within-session retrieval is unambiguous.
"""
from __future__ import annotations

import random
from dataclasses import dataclass, field

from llmlab.models.local_model import SamplingConfig


@dataclass(frozen=True)
class Fact:
    statement: str
    question: str
    answer: str


@dataclass
class Turn:
    text: str
    is_fact: bool
    fact_index: int = -1


@dataclass
class Session:
    turns: list
    facts: list
    positions: dict = field(default_factory=dict)  # fact_index -> turn index

    def recall_items(self) -> list:
        """[(fact, distance_in_turns), ...] — distance from its turn to the end."""
        end = len(self.turns)
        return [(self.facts[i], end - self.positions[i]) for i in range(len(self.facts))]


FACT_BANK: list = [
    Fact("My flight to Tokyo is flight DL482.", "What is my flight number to Tokyo?", "DL482"),
    Fact("The staging API key is sk-7731.", "What is the staging API key?", "sk-7731"),
    Fact("I parked on level P4 of the garage.", "Which garage level did I park on?", "P4"),
    Fact("The standup moved to room B12.", "Which room is the standup in?", "B12"),
    Fact("My locker combination is 24-19-7.", "What is my locker combination?", "24-19-7"),
    Fact("The release is tagged v3.9.1.", "What tag is the release?", "v3.9.1"),
    Fact("The office wifi password is rocket-42.", "What is the office wifi password?", "rocket-42"),
    Fact("My new desk is number D207.", "What is my desk number?", "D207"),
    Fact("The client's account ID is ACC-5590.", "What is the client's account ID?", "ACC-5590"),
    Fact("The promo code for the demo is SAVE15.", "What is the demo promo code?", "SAVE15"),
    Fact("My rental car's plate is KZ-8841.", "What is my rental car's plate?", "KZ-8841"),
    Fact("The conference is in hall H7.", "Which hall is the conference in?", "H7"),
    Fact("The database shard is named shard-delta.", "What is the database shard named?", "shard-delta"),
    Fact("The invoice total came to 4820 dollars.", "What was the invoice total in dollars?", "4820"),
    Fact("The server room door code is 9305.", "What is the server room door code?", "9305"),
    Fact("My badge number is BR-3162.", "What is my badge number?", "BR-3162"),
]

FILLER: list = [
    "By the way, the weather has been lovely this week.",
    "I grabbed a coffee on the way in this morning.",
    "That was a productive discussion earlier.",
    "I think the team is in good spirits today.",
    "Let's keep the momentum going.",
    "The cafeteria added a new sandwich option.",
    "Traffic was light on the commute today.",
    "I might repaint the fence this weekend.",
    "Anyway, thanks for keeping track of all this.",
    "Remind me to stretch now and then.",
]


def make_sessions(n_sessions: int = 5, n_facts: int = 8, spacing: int = 2, seed: int = 0) -> list:
    rng = random.Random(seed)
    sessions = []
    for _ in range(n_sessions):
        facts = rng.sample(FACT_BANK, n_facts)
        turns, positions = [], {}
        for i, fact in enumerate(facts):
            positions[i] = len(turns)
            turns.append(Turn(fact.statement, True, i))
            for _ in range(spacing):
                turns.append(Turn(rng.choice(FILLER), False))
        sessions.append(Session(turns, facts, positions))
    return sessions


def render_window(turns: list, window=None) -> str:
    visible = turns[-window:] if window else turns
    return "\n".join(f"- {t.text}" for t in visible)


_WINDOW_SYSTEM = (
    "You are given recent conversation notes. Answer the question using ONLY them. "
    "If the answer is not in the notes, reply exactly: I don't know."
)


def answer_from_window(model, turns: list, question: str, window: int, sampling=None):
    """No-memory baseline: answer from only the last ``window`` turns. ``(text, new_tokens)``."""
    messages = [
        {"role": "system", "content": _WINDOW_SYSTEM},
        {"role": "user", "content": f"Conversation notes:\n{render_window(turns, window)}\n\nQuestion: {question}"},
    ]
    result = model.generate(messages, sampling or SamplingConfig(max_new_tokens=32))
    return result.text.strip(), result.new_tokens
