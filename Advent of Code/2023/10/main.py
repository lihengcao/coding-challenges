"""
day 10
"""

from typing import Optional
from collections import deque

INPUT = "input.txt"
DEBUG = False

INPUT = "sample.txt"
DEBUG = True

CUR_TO_NEXT_MAPPINGS = {  # (i, j) coords, not (x, y)
    '|': ((-1, 0), (1, 0)),
    '-': ((0, -1), (0, 1)),
    'L': ((-1, 0), (0, 1)),
    'J': ((-1, 0), (0, -1)),
    '7': ((0, -1), (1, 0)),
    'F': ((0, 1), (1, 0)),
}

DIRECTIONS = (
    (1, 0), 
    (0, 1),
    (-1, 0),
    (0, -1),
)

def get_start(grid: list[str]) -> tuple[int, int]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                return i, j
            
    return 0, 0


def traverse(grid: list[str], start_i: int, start_j: int) -> Optional[tuple[int, set[tuple[int, int]]]]:
     # easier to track visited than travel directoin
    visited = set() 
    q = deque([(start_i, start_j)])
    m, n = len(grid), len(grid[0])

    length = 0

    while q:
        x, y = q.popleft()
        # print(x, y)

        if not (0 <= x < m and 0 <= y < n) or (x, y,) in visited:
            continue

        char = grid[x][y]

        if char == 'S':
            if length == 1:
                continue
            return length, visited
        
        if char == '.':
            return None
        
        length += 1
        
        visited.add((x, y,))

        for dx, dy in CUR_TO_NEXT_MAPPINGS[char]:
            i, j = x + dx, y + dy
            if not (0 <= i < m and 0 <= j < n):
                return None
            if (i, j,) not in visited:
                q.append((i, j,))
    

    return None



def p1() -> None:
    """part 1"""
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    i, j = get_start(lines)
    print(i, j)

    loop = 0
    for di, dj in DIRECTIONS:
        a = traverse(lines, i + di, j + dj)
        print(a)
        if a is not None:
            a, _ = a
            # this is a nongeneric hacky solution for my input ):
            loop = max(loop, a + 1)

    print(loop // 2)


def count_inside_loop(grid: list[str], boundary: set[tuple[int, int]], visited: set[tuple[int, int]], i: int, j: int) -> int:
    inside_loop = 0
    m, n = len(grid), len(grid[0])

    stack = [(i, j)]

    while stack:
        x, y = stack.pop()
        # print(x, y, stack)

        if (x, y) in visited or (x, y) in boundary:
            continue
            
        visited.add((x, y))

        if not (0 <= x < m and 0 <= y < n):
            return 0
        
        char = grid[x][y]
        # print(char)

        if char == 'S':
            continue

        if char != '.' and (x, y) not in boundary:
            return 0
    
        inside_loop += 1

        for dx, dy in DIRECTIONS:
            i, j = x + dx, y + dy
            stack.append((i, j))
    # print(inside_loop, i, j)
    return inside_loop


def p2():
    """part 2"""
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    i, j = get_start(lines)

    loop = 0
    boundary = None
    for di, dj in DIRECTIONS:
        a = traverse(lines, i + di, j + dj)
        if a is None:
            continue

        a, v = a
        if a + 1 > loop:
            # this is a nongeneric hacky solution for my input ):
            loop = a + 1
            boundary = v

    print(loop//2)

    assert boundary is not None
    visited = set()
    enclosed = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '.':
                enclosed += count_inside_loop(lines, boundary, visited, i, j)

    # print(count_inside_loop(lines, visited, 6, 2))

    print(enclosed)

p2()



