"""Pull a final numeric answer out of free-form model text (Notebook 06).

Robust extraction is half the battle in any reasoning eval: the same model is
"correct" or not depending on how you parse it. Priority order:

1. an explicit GSM ``#### N`` marker,
2. the last ``answer is / = / : N`` cue (so we read the *conclusion*, not an
   intermediate step),
3. otherwise the last number in the text (the common CoT heuristic).
"""
from __future__ import annotations

import re
from typing import Optional

_NUMBER = r"-?\d[\d,]*(?:\.\d+)?"
_HASH = re.compile(r"####\s*\$?(" + _NUMBER + r")")
_CUE = re.compile(r"(?:answer|result|total)\b[^\d\-]{0,15}?(" + _NUMBER + r")", re.IGNORECASE)
_ANY = re.compile(_NUMBER)


def _to_float(token: str) -> float:
    return float(token.replace(",", ""))


def extract_answer(text: Optional[str]) -> Optional[float]:
    if not text:
        return None
    hashed = _HASH.search(text)
    if hashed:
        return _to_float(hashed.group(1))
    cues = list(_CUE.finditer(text))
    if cues:
        return _to_float(cues[-1].group(1))
    numbers = _ANY.findall(text)
    if numbers:
        return _to_float(numbers[-1])
    return None


def is_correct(pred: Optional[float], gold: float, tol: float = 1e-6) -> bool:
    return pred is not None and abs(pred - gold) <= tol
