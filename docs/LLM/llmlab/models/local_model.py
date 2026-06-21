"""A Hugging Face / PyTorch backend for local inference (Notebook 02).

This is the *observable* runtime: unlike a server or a high-level framework, we
can reach into the forward pass (logits, hidden states, attention, the KV cache)
and we can re-implement decoding by hand. MLX (Notebook 03) and llama.cpp
(Notebook 04) backends will sit behind the same ``LocalModel`` shape later.

Imports of torch/transformers are deferred so that ``import`` of this module
(and the dataclasses below) stays cheap for fast unit tests.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterator, Optional, Sequence, Union

Message = dict  # {"role": str, "content": str}
PromptInput = Union[str, Sequence[Message]]


@dataclass
class SamplingConfig:
    """Decoding knobs. Defaults are *clean greedy* (deterministic, no penalties).

    We set these explicitly on every ``generate`` call so a model's bundled
    ``generation_config`` (which often defaults to sampling!) can't surprise us.
    """

    max_new_tokens: int = 64
    do_sample: bool = False
    temperature: float = 1.0
    top_k: Optional[int] = None
    top_p: Optional[float] = None
    repetition_penalty: float = 1.0
    seed: Optional[int] = None


@dataclass
class GenerationResult:
    text: str
    prompt_tokens: int
    new_tokens: int
    token_ids: list = field(default_factory=list)


class LocalModel:
    """Thin, inspectable wrapper around a causal LM + its tokenizer."""

    def __init__(
        self,
        model_id: str,
        device: Optional[str] = None,
        dtype: Optional[str] = None,
        attn_implementation: str = "eager",
    ):
        import torch  # noqa: F401
        from transformers import AutoModelForCausalLM, AutoTokenizer

        from llmlab import config

        self.model_id = model_id
        self.device = device or config.get_device()
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        # `eager` attention is required for `output_attentions=True`; sdpa/flash
        # silently return no attention weights.
        load_kwargs: dict[str, Any] = {"attn_implementation": attn_implementation}
        if dtype is not None:
            load_kwargs["dtype"] = dtype
        self.model = (
            AutoModelForCausalLM.from_pretrained(model_id, **load_kwargs)
            .to(self.device)
            .eval()
        )

    # --- inputs -----------------------------------------------------------
    def to_input(self, prompt: PromptInput, add_generation_prompt: bool = True) -> dict:
        """Turn a raw string or a chat message list into model-ready tensors."""
        if isinstance(prompt, str):
            enc = self.tokenizer(prompt, return_tensors="pt")
        else:
            enc = self.tokenizer.apply_chat_template(
                list(prompt),
                add_generation_prompt=add_generation_prompt,
                return_tensors="pt",
                return_dict=True,
            )
        return {k: v.to(self.device) for k, v in enc.items()}

    @property
    def _pad_id(self):
        return self.tokenizer.pad_token_id or self.tokenizer.eos_token_id

    def _gen_kwargs(self, sampling: SamplingConfig) -> dict:
        kwargs: dict[str, Any] = dict(
            max_new_tokens=sampling.max_new_tokens,
            do_sample=sampling.do_sample,
            repetition_penalty=sampling.repetition_penalty,
            num_beams=1,
            pad_token_id=self._pad_id,
        )
        if sampling.do_sample:
            kwargs.update(
                temperature=sampling.temperature,
                top_k=sampling.top_k,
                top_p=sampling.top_p,
            )
        return kwargs

    # --- generation -------------------------------------------------------
    def generate(
        self,
        prompt: PromptInput,
        sampling: Optional[SamplingConfig] = None,
        add_generation_prompt: bool = True,
    ) -> GenerationResult:
        import torch

        sampling = sampling or SamplingConfig()
        if sampling.seed is not None:
            torch.manual_seed(sampling.seed)
        inputs = self.to_input(prompt, add_generation_prompt)
        with torch.no_grad():
            out = self.model.generate(**inputs, **self._gen_kwargs(sampling))
        prompt_len = inputs["input_ids"].shape[-1]
        new_ids = out[0, prompt_len:]
        return GenerationResult(
            text=self.tokenizer.decode(new_ids, skip_special_tokens=True),
            prompt_tokens=int(prompt_len),
            new_tokens=int(new_ids.shape[-1]),
            token_ids=new_ids.tolist(),
        )

    def stream(
        self,
        prompt: PromptInput,
        sampling: Optional[SamplingConfig] = None,
        add_generation_prompt: bool = True,
    ) -> Iterator[str]:
        """Yield decoded text chunks as they are generated."""
        from threading import Thread

        from transformers import TextIteratorStreamer

        sampling = sampling or SamplingConfig()
        inputs = self.to_input(prompt, add_generation_prompt)
        streamer = TextIteratorStreamer(
            self.tokenizer, skip_prompt=True, skip_special_tokens=True
        )
        kwargs = {**inputs, **self._gen_kwargs(sampling), "streamer": streamer}
        thread = Thread(target=self.model.generate, kwargs=kwargs)
        thread.start()
        try:
            for chunk in streamer:
                yield chunk
        finally:
            thread.join()

    # --- introspection ----------------------------------------------------
    def forward(
        self,
        prompt: PromptInput,
        output_attentions: bool = False,
        output_hidden_states: bool = False,
        add_generation_prompt: bool = True,
    ) -> tuple[dict, Any]:
        """Run a single forward pass and return ``(inputs, outputs)``."""
        import torch

        inputs = self.to_input(prompt, add_generation_prompt)
        with torch.no_grad():
            outputs = self.model(
                **inputs,
                output_attentions=output_attentions,
                output_hidden_states=output_hidden_states,
                use_cache=True,
            )
        return inputs, outputs


def greedy_decode(
    model,
    input_ids,
    attention_mask=None,
    max_new_tokens: int = 64,
    eos_token_id: Optional[int] = None,
):
    """Hand-written greedy decoding with an incremental KV cache.

    This is exactly what ``model.generate(do_sample=False, repetition_penalty=1.0)``
    does under the hood: prefill once, then feed back one token at a time while
    reusing the cache. Returns the full sequence ``[prompt + generated]``.
    """
    import torch

    model.eval()
    generated = input_ids
    cur_ids = input_ids
    cur_mask = attention_mask
    past = None
    with torch.no_grad():
        for _ in range(max_new_tokens):
            outputs = model(
                input_ids=cur_ids,
                attention_mask=cur_mask,
                past_key_values=past,
                use_cache=True,
            )
            past = outputs.past_key_values
            next_id = outputs.logits[:, -1, :].argmax(dim=-1, keepdim=True)
            generated = torch.cat([generated, next_id], dim=-1)
            if eos_token_id is not None and next_id.item() == eos_token_id:
                break
            cur_ids = next_id  # only the new token; the rest lives in `past`
            if cur_mask is not None:
                cur_mask = torch.cat(
                    [cur_mask, torch.ones_like(next_id)], dim=-1
                )
    return generated


def kv_cache_shapes(past_key_values) -> list:
    """Return ``[(key_shape, value_shape), ...]`` per layer across cache formats.

    transformers has shipped several KV-cache representations; this normalises
    them so notebooks/tests don't depend on a specific version's internals.
    """
    pkv = past_key_values
    if hasattr(pkv, "to_legacy_cache"):
        try:
            legacy = pkv.to_legacy_cache()
            return [(tuple(k.shape), tuple(v.shape)) for (k, v) in legacy]
        except Exception:
            pass
    if hasattr(pkv, "layers"):
        shapes = []
        for layer in pkv.layers:
            k = getattr(layer, "keys", None)
            v = getattr(layer, "values", None)
            if k is not None and v is not None:
                shapes.append((tuple(k.shape), tuple(v.shape)))
        if shapes:
            return shapes
    if isinstance(pkv, (list, tuple)):
        return [(tuple(k.shape), tuple(v.shape)) for (k, v) in pkv]
    return []
