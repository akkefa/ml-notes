"""A runnable long-context recall probe: passkey / needle-in-a-haystack.

This is the experimental core of the memory research. We bury a secret number
inside a long block of filler text at a controllable *depth*, then ask the model
to recall it. Sweeping (length x depth) reveals two classic failures:

- **length degradation**: recall collapses as the context grows;
- **lost in the middle**: needles near the start/end survive, the middle is lost.

Token budgets are approximate (we count filler tokens, not the final templated
prompt), which is fine for a within-model trend study.
"""
from __future__ import annotations

import random
import re
from dataclasses import dataclass
from typing import Optional, Sequence

FILLER_SENTENCE = "The grass is green and the sky is blue and the sun is bright. "
QUESTION = "What is the secret passkey? Reply with only the number."


def make_haystack(
    tokenizer,
    n_tokens: int,
    needle: str,
    depth: float = 0.5,
    filler_sentence: str = FILLER_SENTENCE,
) -> str:
    """Build ~``n_tokens`` of filler with ``needle`` inserted at fractional ``depth``."""
    filler_ids = tokenizer(filler_sentence, add_special_tokens=False)["input_ids"]
    reps = max(1, n_tokens // max(1, len(filler_ids)))
    body = list(filler_ids) * reps
    needle_ids = tokenizer(needle, add_special_tokens=False)["input_ids"]
    pos = int(len(body) * min(max(depth, 0.0), 1.0))
    body = body[:pos] + list(needle_ids) + body[pos:]
    return tokenizer.decode(body)


def passkey_messages(
    tokenizer,
    passkey: int,
    n_tokens: int,
    depth: float = 0.5,
) -> list:
    """Chat messages embedding a passkey at ``depth`` inside an ``n_tokens`` haystack."""
    needle = f" The secret passkey is {passkey}. Remember it. "
    haystack = make_haystack(tokenizer, n_tokens, needle, depth)
    return [{"role": "user", "content": f"{haystack}\n\n{QUESTION}"}]


def recall_hit(generated_text: str, passkey: int) -> bool:
    """True if the passkey appears as a standalone number in the output."""
    numbers = re.findall(r"\d+", generated_text)
    return str(passkey) in numbers


@dataclass
class PasskeyResult:
    n_tokens: int
    depth: float
    passkey: int
    answer: str
    hit: bool
    prompt_tokens: int


def run_passkey_grid(
    local_model,
    lengths: Sequence[int],
    depths: Sequence[float],
    max_new_tokens: int = 12,
    seed: int = 0,
) -> list:
    """Evaluate single-needle recall over a (length x depth) grid on a ``LocalModel``.

    Note: a *single* needle in low-entropy filler is easy — modern small models
    ace it for thousands of tokens because the lone number simply stands out.
    Use ``run_multikey_grid`` for a probe that actually exposes the cliff.
    """
    from llmlab.models.local_model import SamplingConfig

    rng = random.Random(seed)
    results = []
    for n_tokens in lengths:
        for depth in depths:
            passkey = rng.randint(10000, 99999)
            messages = passkey_messages(local_model.tokenizer, passkey, n_tokens, depth)
            res = local_model.generate(messages, SamplingConfig(max_new_tokens=max_new_tokens))
            results.append(
                PasskeyResult(
                    n_tokens=int(n_tokens),
                    depth=float(depth),
                    passkey=passkey,
                    answer=res.text.strip(),
                    hit=recall_hit(res.text, passkey),
                    prompt_tokens=res.prompt_tokens,
                )
            )
    return results


# --- harder probe: many near-identical distractor keys ---------------------
def multikey_haystack(
    tokenizer,
    n_tokens: int,
    values: Sequence[int],
    filler_sentence: str = FILLER_SENTENCE,
) -> str:
    """Spread ``Passkey number i is V.`` lines uniformly through ~``n_tokens`` of filler.

    Every line is structurally identical, so the model can't rely on a number
    "popping out" — it must locate the *specific* index requested. That is what
    makes this reveal length-degradation and lost-in-the-middle.
    """
    filler_ids = tokenizer(filler_sentence, add_special_tokens=False)["input_ids"]
    reps = max(1, n_tokens // max(1, len(filler_ids)))
    body = list(filler_ids) * reps
    n_keys = len(values)
    seg = max(1, len(body) // (n_keys + 1))
    parts: list[str] = []
    for i, value in enumerate(values):
        parts.append(tokenizer.decode(body[i * seg:(i + 1) * seg]))
        parts.append(f" Passkey number {i + 1} is {value}. ")
    parts.append(tokenizer.decode(body[n_keys * seg:]))
    return "".join(parts)


def multikey_messages(
    tokenizer,
    n_tokens: int,
    values: Sequence[int],
    query_index: int,
) -> list:
    document = multikey_haystack(tokenizer, n_tokens, values)
    question = f"What is passkey number {query_index + 1}? Reply with only the number."
    return [{"role": "user", "content": f"{document}\n\n{question}"}]


@dataclass
class MultiKeyResult:
    n_tokens: int
    n_keys: int
    query_index: int
    depth: float
    target: int
    answer: str
    hit: bool
    prompt_tokens: int


def run_multikey_grid(
    local_model,
    lengths: Sequence[int],
    n_keys: int = 10,
    max_new_tokens: int = 12,
    seed: int = 0,
) -> list:
    """Query every one of ``n_keys`` planted keys at each context length.

    ``depth = query_index / (n_keys - 1)`` gives a (length x position) grid that
    cleanly separates length-degradation from lost-in-the-middle.
    """
    from llmlab.models.local_model import SamplingConfig

    rng = random.Random(seed)
    results = []
    for n_tokens in lengths:
        values = [rng.randint(10000, 99999) for _ in range(n_keys)]
        for query_index in range(n_keys):
            messages = multikey_messages(local_model.tokenizer, n_tokens, values, query_index)
            res = local_model.generate(messages, SamplingConfig(max_new_tokens=max_new_tokens))
            depth = query_index / (n_keys - 1) if n_keys > 1 else 0.0
            results.append(
                MultiKeyResult(
                    n_tokens=int(n_tokens),
                    n_keys=n_keys,
                    query_index=query_index,
                    depth=round(depth, 3),
                    target=values[query_index],
                    answer=res.text.strip(),
                    hit=recall_hit(res.text, values[query_index]),
                    prompt_tokens=res.prompt_tokens,
                )
            )
    return results
