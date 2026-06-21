"""Tools and a tiny registry for the from-scratch agent (Notebook 07).

A *tool* is a name + description + a callable ``run(args: dict) -> str``. The
registry renders tool specs into the system prompt and dispatches calls,
turning every failure (unknown tool, bad args, runtime error) into a plain
observation string the model can read and recover from.

The calculator evaluates arithmetic with the ``ast`` module — never ``eval`` —
so a hallucinated ``__import__(...)`` is a parse error, not code execution.
"""
from __future__ import annotations

import ast
import operator
from dataclasses import dataclass
from typing import Callable

FINAL_ANSWER = "final_answer"

_BINOPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
_UNARYOPS = {ast.USub: operator.neg, ast.UAdd: operator.pos}


def _eval_node(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _BINOPS:
        return _BINOPS[type(node.op)](_eval_node(node.left), _eval_node(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARYOPS:
        return _UNARYOPS[type(node.op)](_eval_node(node.operand))
    raise ValueError("unsupported expression")


def calculate(expression: str) -> float:
    """Safely evaluate an arithmetic expression (numbers and + - * / // % ** only)."""
    tree = ast.parse(expression, mode="eval")
    return _eval_node(tree.body)


def format_number(value) -> str:
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


@dataclass
class Tool:
    name: str
    description: str
    run: Callable[[dict], str]
    args_hint: str


def _calculator_run(args: dict) -> str:
    expression = args.get("expression")
    if expression is None:
        return "Error: calculator needs an 'expression' argument."
    # Models often write '^' for exponentiation; in Python that is bitwise-xor,
    # so normalise it to '**' before evaluating (a real calculator's UX).
    normalised = str(expression).replace("^", "**")
    try:
        return format_number(calculate(normalised))
    except Exception as exc:  # noqa: BLE001 - report any parse/eval failure to the model
        return f"Error: could not evaluate '{expression}' ({exc})."


class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        self._tools[tool.name] = tool

    def tools(self) -> list:
        return list(self._tools.values())

    def names(self) -> list:
        return list(self._tools)

    def call(self, name: str, args) -> str:
        tool = self._tools.get(name)
        if tool is None:
            return f"Error: unknown tool '{name}'. Available tools: {', '.join(self.names())}."
        if not isinstance(args, dict):
            return f"Error: 'args' must be a JSON object for tool '{name}'."
        try:
            return tool.run(args)
        except Exception as exc:  # noqa: BLE001 - never let a tool crash the loop
            return f"Error while running '{name}': {exc}"


def make_default_registry() -> ToolRegistry:
    """A calculator plus the built-in ``final_answer`` action."""
    registry = ToolRegistry()
    registry.register(Tool(
        name="calculator",
        description="evaluate an arithmetic expression and return the number.",
        run=_calculator_run,
        args_hint='{"expression": "<math expression, e.g. 24 - 9 - 7>"}',
    ))
    registry.register(Tool(
        name=FINAL_ANSWER,
        description="give your final answer and stop.",
        run=lambda args: format_number(args.get("answer", "")) if isinstance(args.get("answer"), (int, float)) else str(args.get("answer", "")),
        args_hint='{"answer": "<final number>"}',
    ))
    return registry
