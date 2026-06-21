"""Reasoning prompt strategies as message builders (Notebook 06).

Each function maps a question to a chat-message list. Keeping them as plain
functions ``question -> messages`` lets the harness treat "strategy" as a
first-class, swappable variable.
"""
from __future__ import annotations

from typing import Sequence, Tuple

DIRECT_SYSTEM = "You are a precise calculator. Give only the final number, with no words or working."
COT_SYSTEM = (
    "You are a careful problem solver. Work through the problem step by step, "
    "then finish with a line of the exact form: 'The answer is <number>.'"
)


def direct_messages(question: str) -> list:
    """Zero-shot, answer-only. Suppresses reasoning to isolate its value."""
    return [
        {"role": "system", "content": DIRECT_SYSTEM},
        {"role": "user", "content": f"{question}\nReply with only the final number."},
    ]


def cot_messages(question: str) -> list:
    """Zero-shot chain-of-thought."""
    return [
        {"role": "system", "content": COT_SYSTEM},
        {"role": "user", "content": f"{question}\nThink step by step, then end with 'The answer is <number>.'"},
    ]


def fewshot_cot_messages(question: str, exemplars: Sequence[Tuple[str, str]]) -> list:
    """Few-shot CoT: worked examples as prior user/assistant turns."""
    messages = [{"role": "system", "content": COT_SYSTEM}]
    for example_q, example_solution in exemplars:
        messages.append({"role": "user", "content": example_q})
        messages.append({"role": "assistant", "content": example_solution})
    messages.append({"role": "user", "content": question})
    return messages
