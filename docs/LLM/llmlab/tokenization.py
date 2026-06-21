"""Tokenizer inspection + manual chat-template rendering (Notebook 01).

Two jobs:

1. Look *inside* BPE tokenization (:func:`token_table`) to see exactly how text
   becomes integers.
2. Reproduce ``tokenizer.apply_chat_template(..., tokenize=False)``
   byte-for-byte for the major template families, so we understand the precise
   string a chat model is trained to expect.

The hand-rolled renderers exist for *learning*. In real code, always call the
tokenizer's official template - see the Llama-3.1 note in the notebook for why
hand-rolling is fragile (dynamic dates, tool blocks, version drift).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional, Sequence

Message = dict  # {"role": str, "content": str}

# Default system prompts some instruct templates silently inject when the
# caller provides none. Discovered empirically from each tokenizer.
SMOLLM2_DEFAULT_SYSTEM = "You are a helpful AI assistant named SmolLM, trained by Hugging Face"
QWEN_DEFAULT_SYSTEM = "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."


def load_tokenizer(model_id: str):
    """Thin wrapper so notebooks/tests don't import transformers everywhere."""
    from transformers import AutoTokenizer

    return AutoTokenizer.from_pretrained(model_id)


@dataclass
class TokenRow:
    pos: int
    token_id: int
    piece: str  # raw subword piece, e.g. 'ĠParis' (byte-level) or '▁Paris' (spm)
    text: str   # this single token decoded back to text


def token_table(tokenizer, text: str, add_special_tokens: bool = False) -> list[TokenRow]:
    """Tokenize ``text`` and return one row per token: id, raw piece, decoded text."""
    ids = tokenizer.encode(text, add_special_tokens=add_special_tokens)
    pieces = tokenizer.convert_ids_to_tokens(ids)
    return [
        TokenRow(pos=pos, token_id=int(tid), piece=piece, text=tokenizer.decode([tid]))
        for pos, (tid, piece) in enumerate(zip(ids, pieces))
    ]


def render_chatml(
    messages: Sequence[Message],
    add_generation_prompt: bool = True,
    default_system: Optional[str] = None,
) -> str:
    """ChatML renderer (Qwen, SmolLM2, OpenHermes, ...).

    Per message: ``<|im_start|>{role}\\n{content}<|im_end|>\\n``. If
    ``default_system`` is set and no system message is present, it is prepended
    (this is what Qwen2.5 / SmolLM2 do under the hood).
    """
    msgs = list(messages)
    if default_system is not None and (not msgs or msgs[0]["role"] != "system"):
        msgs = [{"role": "system", "content": default_system}, *msgs]
    out = "".join(
        f"<|im_start|>{m['role']}\n{m['content']}<|im_end|>\n" for m in msgs
    )
    if add_generation_prompt:
        out += "<|im_start|>assistant\n"
    return out


def render_llama3(messages: Sequence[Message], add_generation_prompt: bool = True) -> str:
    """Llama-3(.0) header renderer.

    ``<|begin_of_text|>`` then per message
    ``<|start_header_id|>{role}<|end_header_id|>\\n\\n{content}<|eot_id|>``.
    Content is stripped, matching the official ``{{ content | trim }}``.
    """
    out = "<|begin_of_text|>"
    for m in messages:
        out += (
            f"<|start_header_id|>{m['role']}<|end_header_id|>\n\n"
            f"{m['content'].strip()}<|eot_id|>"
        )
    if add_generation_prompt:
        out += "<|start_header_id|>assistant<|end_header_id|>\n\n"
    return out


def render_mistral_inst(messages: Sequence[Message]) -> str:
    """Mistral v0.2/v0.3 ``[INST]`` renderer.

    There is no system *role*: a leading system message is merged into the first
    user turn as ``system\\n\\nuser``. Each user turn is wrapped
    ``[INST] ... [/INST]``; assistant turns are emitted verbatim then ``</s>``.
    There is no separate generation-prompt suffix.
    """
    out = "<s>"
    msgs = list(messages)
    system: Optional[str] = None
    if msgs and msgs[0]["role"] == "system":
        system = msgs.pop(0)["content"]
    for m in msgs:
        if m["role"] == "user":
            content = m["content"]
            if system is not None:
                content = f"{system}\n\n{content}"
                system = None
            out += f"[INST] {content}[/INST]"
        elif m["role"] == "assistant":
            out += f"{m['content']}</s>"
    return out


def first_diff(a: str, b: str, window: int = 24) -> str:
    """Human-readable description of the first byte where two strings diverge."""
    if a == b:
        return "identical"
    limit = min(len(a), len(b))
    i = 0
    while i < limit and a[i] == b[i]:
        i += 1
    lo = max(0, i - window)
    return (
        f"first diff at index {i} (len official={len(a)}, ours={len(b)})\n"
        f"  official: ...{a[lo:i + window]!r}\n"
        f"  ours    : ...{b[lo:i + window]!r}"
    )


def verify_render(
    tokenizer,
    messages: Sequence[Message],
    renderer: Callable[..., str],
    *,
    add_generation_prompt: bool = True,
    **renderer_kwargs,
) -> tuple[bool, str, str]:
    """Compare a hand-rolled renderer to the official template byte-for-byte.

    Returns ``(matches, official_string, our_string)``.
    """
    official = tokenizer.apply_chat_template(
        list(messages), tokenize=False, add_generation_prompt=add_generation_prompt
    )
    try:
        ours = renderer(messages, add_generation_prompt=add_generation_prompt, **renderer_kwargs)
    except TypeError:
        # Renderers without an add_generation_prompt arg (e.g. Mistral).
        ours = renderer(messages, **renderer_kwargs)
    return official == ours, official, ours
