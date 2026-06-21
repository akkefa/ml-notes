"""Extract the agent's JSON action from messy model output (Notebook 07).

Small models wrap JSON in prose or ```json fences and sometimes emit a whole
fake trajectory. We scan for the first balanced ``{...}`` that parses as a JSON
object and return it; everything around it is ignored. Returns ``None`` when no
valid object is present, which the loop turns into a corrective observation.
"""
from __future__ import annotations

import json
from typing import Optional


def extract_json(text: Optional[str]) -> Optional[dict]:
    if not text:
        return None
    start = text.find("{")
    while start != -1:
        depth = 0
        for i in range(start, len(text)):
            char = text[i]
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    candidate = text[start:i + 1]
                    try:
                        parsed = json.loads(candidate)
                    except json.JSONDecodeError:
                        break  # unbalanced/invalid; restart scan after this '{'
                    if isinstance(parsed, dict):
                        return parsed
                    break
        start = text.find("{", start + 1)
    return None
