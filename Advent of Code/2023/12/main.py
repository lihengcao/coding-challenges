"""
day 11
"""

from collections import deque
from typing import Optional

INPUT = "input.txt"
DEBUG = False

# INPUT = "sample.txt"
DEBUG = True


def p1() -> None:
    """part 1"""
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
