"""A small, self-contained GSM-style reasoning task set (Notebook 06).

Hand-written multi-step word problems with integer answers. Self-contained (no
dataset download), deterministic, and just hard enough that single-shot "direct"
answering trails chain-of-thought on a small model. Exemplars for few-shot
prompting are kept *separate* from the eval set to avoid leakage.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    id: str
    question: str
    answer: int
    category: str


GSM_TASKS: list[Task] = [
    Task("t01", "A baker bakes 24 muffins. He sells 9 in the morning and 7 in the "
         "afternoon. How many muffins are left?", 8, "arithmetic"),
    Task("t02", "Tom buys 3 packs of pencils with 12 pencils in each pack. He gives "
         "10 pencils to his friends. How many pencils does Tom have left?", 26, "arithmetic"),
    Task("t03", "A train travels at 60 km/h for 2 hours and then at 80 km/h for 1 "
         "hour. How many kilometers does it travel in total?", 200, "rates"),
    Task("t04", "Sarah has 50 dollars. She buys 4 notebooks costing 6 dollars each. "
         "How many dollars does she have left?", 26, "money"),
    Task("t05", "A classroom has 5 rows of desks with 6 desks in each row. If 8 desks "
         "are empty, how many desks are occupied?", 22, "arithmetic"),
    Task("t06", "A water tank holds 200 liters. It loses 15 liters per day. How many "
         "liters remain after 7 days?", 95, "rates"),
    Task("t07", "Mark reads 18 pages each day for 5 days. The book has 100 pages. How "
         "many pages are left to read?", 10, "arithmetic"),
    Task("t08", "A store had 120 apples. They sold three quarters of them. How many "
         "apples are left?", 30, "fractions"),
    Task("t09", "Lucy earns 15 dollars per hour. She works 6 hours on Monday and 4 "
         "hours on Tuesday. How many dollars does she earn in total?", 150, "money"),
    Task("t10", "A rectangle is 8 cm long and 5 cm wide. What is its perimeter in "
         "centimeters?", 26, "geometry"),
    Task("t11", "There are 32 students split into groups of 4. Each group needs 2 "
         "markers. How many markers are needed in total?", 16, "arithmetic"),
    Task("t12", "John saves 7 dollars each week. How many dollars does he save in 12 "
         "weeks?", 84, "money"),
    Task("t13", "A farmer counts 45 chickens and 27 cows. Chickens have 2 legs and "
         "cows have 4 legs. How many animal legs are there in total?", 198, "arithmetic"),
    Task("t14", "A pizza is cut into 8 slices. Three friends each eat 2 slices. How "
         "many slices are left?", 2, "arithmetic"),
]


# Large-number tasks: the *setup* is trivial (1–2 operations) but the arithmetic
# is far beyond a 0.5B model's reliable mental math. These isolate the value of an
# exact calculator tool from the model's planning ability.
HARD_ARITHMETIC_TASKS: list[Task] = [
    Task("h01", "What is 4877 multiplied by 619?", 3018863, "hard-arithmetic"),
    Task("h02", "A factory makes 1234 widgets per day. How many widgets does it make "
         "in 365 days?", 450410, "hard-arithmetic"),
    Task("h03", "Subtract 4321 from 98765, then multiply the result by 7.", 661108, "hard-arithmetic"),
    Task("h04", "What is 7 raised to the power of 6?", 117649, "hard-arithmetic"),
    Task("h05", "A warehouse has 84 pallets. Each pallet holds 156 boxes. How many "
         "boxes are there in total?", 13104, "hard-arithmetic"),
]


# (question, worked_solution) pairs for few-shot prompting — NOT in the eval set.
FEWSHOT_EXEMPLARS: list[tuple[str, str]] = [
    (
        "A shop has 15 red balloons and 9 blue balloons. They sell 6 balloons. "
        "How many balloons are left?",
        "There are 15 + 9 = 24 balloons in total. After selling 6, there are "
        "24 - 6 = 18 left. The answer is 18.",
    ),
    (
        "Ann has 4 boxes with 7 candies in each box. She eats 5 candies. How many "
        "candies remain?",
        "There are 4 x 7 = 28 candies. After eating 5, there are 28 - 5 = 23 "
        "remaining. The answer is 23.",
    ),
    (
        "A car drives at 50 km/h for 3 hours. How far does it travel?",
        "Distance = speed x time = 50 x 3 = 150 km. The answer is 150.",
    ),
]
