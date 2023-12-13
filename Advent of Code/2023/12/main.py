"""
day 11
"""

from typing import Optional
from collections import deque

INPUT = "input.txt"
DEBUG = False

# INPUT = "sample.txt"
DEBUG = True

def p1() -> None:
    """part 1"""
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    