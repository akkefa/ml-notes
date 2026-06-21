"""Run reasoning strategies over a task set and score them (Notebook 06).

The harness is deliberately tiny and transparent: one record per (task,
strategy) trial, aggregated into accuracy + cost. ``self_consistency`` samples
several chains per task and takes the majority answer. This same shape will back
the agent/memory evals later in the lab.
"""
from __future__ import annotations

import time
from collections import Counter
from dataclasses import dataclass, field
from typing import Callable, Optional, Sequence

from llmlab.evals.extract import extract_answer, is_correct

StrategyFn = Callable[[str], list]


@dataclass
class EvalRecord:
    task_id: str
    category: str
    strategy: str
    pred: Optional[float]
    gold: float
    correct: bool
    new_tokens: int
    latency_s: float
    output: str


@dataclass
class StrategyReport:
    strategy: str
    accuracy: float
    avg_new_tokens: float
    avg_latency_s: float
    n: int
    records: list = field(default_factory=list)


def _aggregate(strategy: str, records: Sequence[EvalRecord]) -> StrategyReport:
    n = len(records)
    if n == 0:
        return StrategyReport(strategy, 0.0, 0.0, 0.0, 0, [])
    return StrategyReport(
        strategy=strategy,
        accuracy=sum(r.correct for r in records) / n,
        avg_new_tokens=sum(r.new_tokens for r in records) / n,
        avg_latency_s=sum(r.latency_s for r in records) / n,
        n=n,
        records=list(records),
    )


def evaluate(local_model, tasks, strategy_fn: StrategyFn, label: str, sampling=None) -> StrategyReport:
    """Run one strategy (greedy by default) over every task."""
    from llmlab.models.local_model import SamplingConfig

    sampling = sampling or SamplingConfig(max_new_tokens=256)
    records = []
    for task in tasks:
        t0 = time.perf_counter()
        result = local_model.generate(strategy_fn(task.question), sampling)
        latency = time.perf_counter() - t0
        pred = extract_answer(result.text)
        records.append(
            EvalRecord(
                task_id=task.id,
                category=task.category,
                strategy=label,
                pred=pred,
                gold=float(task.answer),
                correct=is_correct(pred, task.answer),
                new_tokens=result.new_tokens,
                latency_s=latency,
                output=result.text,
            )
        )
    return _aggregate(label, records)


def self_consistency(
    local_model,
    tasks,
    strategy_fn: StrategyFn,
    label: str = "self-consistency",
    k: int = 5,
    temperature: float = 0.7,
    top_p: float = 0.95,
    max_new_tokens: int = 256,
) -> StrategyReport:
    """Sample ``k`` chains per task and take the majority-voted answer."""
    from llmlab.models.local_model import SamplingConfig

    records = []
    for task in tasks:
        votes: list[float] = []
        total_tokens = 0
        t0 = time.perf_counter()
        for sample_idx in range(k):
            sampling = SamplingConfig(
                max_new_tokens=max_new_tokens,
                do_sample=True,
                temperature=temperature,
                top_p=top_p,
                seed=sample_idx,
            )
            result = local_model.generate(strategy_fn(task.question), sampling)
            total_tokens += result.new_tokens
            answer = extract_answer(result.text)
            if answer is not None:
                votes.append(answer)
        latency = time.perf_counter() - t0
        pred = Counter(votes).most_common(1)[0][0] if votes else None
        records.append(
            EvalRecord(
                task_id=task.id,
                category=task.category,
                strategy=label,
                pred=pred,
                gold=float(task.answer),
                correct=is_correct(pred, task.answer),
                new_tokens=total_tokens,
                latency_s=latency,
                output=f"votes={votes}",
            )
        )
    return _aggregate(label, records)
