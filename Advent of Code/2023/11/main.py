"""
day 11
"""

from collections import deque
from typing import Optional

INPUT = "input.txt"
DEBUG = False

# INPUT = "sample.txt"
DEBUG = True


def get_expanded_image(lines: list[str]) -> list[list[str]]:
    m, n = len(lines), len(lines[0])
    rows_to_expand_reversed = [
        i for i in range(m - 1, -1, -1) if lines[i].find("#") == -1
    ]
    cols_to_expand = [i for i in range(n) if all(lines[j][i] != "#" for j in range(m))]

    out = []
    for row in range(m):
        if rows_to_expand_reversed and rows_to_expand_reversed[-1] == row:
            out.append(["."] * (n + len(cols_to_expand)))
            rows_to_expand_reversed.pop()

        expand_i = 0
        out.append([])
        for col in range(n):
            if expand_i < len(cols_to_expand) and col == cols_to_expand[expand_i]:
                out[-1].append(".")
                expand_i += 1

            out[-1].append(lines[row][col])

    return out


def calc_distances(galaxy_id_to_location: list[tuple[int, int]]) -> int:
    total_distance = 0
    for i in range(len(galaxy_id_to_location) - 1):
        for j in range(i + 1, len(galaxy_id_to_location)):
            a, b, x, y = *galaxy_id_to_location[i], *galaxy_id_to_location[j]
            total_distance += abs(a - x) + abs(b - y)

    return total_distance


def p1() -> None:
    """part 1"""
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    expanded_image = get_expanded_image(lines)

    galaxy_id_to_location = []

    for i in range(len(expanded_image)):
        for j in range(len(expanded_image[0])):
            if expanded_image[i][j] == "#":
                galaxy_id_to_location.append((i, j))

    print(calc_distances(galaxy_id_to_location))


def bsearch(arr: list[int], target: int) -> int:
    if target > arr[-1]:
        return len(arr)

    lo, hi = 0, len(arr) - 1

    while lo < hi:
        m = (lo + hi) // 2

        if arr[m] < target:
            lo = m + 1
        else:
            hi = m

    return lo


EXPANSION = 1_000_000 - 1


def p2() -> None:
    """part 2"""
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    m, n = len(lines), len(lines[0])

    rows_to_expand = [i for i in range(m) if lines[i].find("#") == -1]
    cols_to_expand = [i for i in range(n) if all(lines[j][i] != "#" for j in range(m))]

    galaxy_id_to_location = []

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                galaxy_id_to_location.append((i, j))

    expanded_locations = []

    for x, y in galaxy_id_to_location:
        x_padding, y_padding = bsearch(rows_to_expand, x), bsearch(cols_to_expand, y)

        expanded_locations.append(
            (x + x_padding * EXPANSION, y + y_padding * EXPANSION)
        )

    print(calc_distances(expanded_locations))


p2()
