# hill climbing

from collections import deque
from collections.abc import Callable


filename = "input.txt"
# filename = "sample.txt"

with open(filename, "r") as f:
    heightmap = [list(l.strip()) for l in f.readlines()]


def search_for(matrix: list[list[str]], target: str) -> tuple[int, int] | None:
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == target:
                return r, c

S, E = search_for(heightmap, 'S'), search_for(heightmap, 'E')
heightmap[S[0]][S[1]] = 'a'
heightmap[E[0]][E[1]] = 'z'


def bfs(grid: list[list[str]], start: tuple[int, int], end: set[tuple[int, int]], move_condition: Callable[[int, int], int]) -> int:
    q: deque[tuple[int, int]] = deque([start])
    steps = 0
    visited = set()

    while q:
        new = deque()
        
        while q:
            cur = q.popleft()
            
            if cur in end:
                return steps

            if cur in visited:
                continue
            visited.add(cur)
            
            
            i, j = cur
            h = ord(grid[i][j])

            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]) and move_condition(h, ord(grid[i + di][j + dj])):
                    new.append((i + di, j + dj))

        q = new
        steps += 1


def first() -> int:
    return bfs(heightmap, S, set([E]), lambda s, e: s + 1 >= e)


def second() -> int:
    a = set()
    for r in range(len(heightmap)):
        for c in range(len(heightmap[0])):
            if heightmap[r][c] == 'a':
                a.add((r, c))
    
    return bfs(heightmap, E, a, lambda s, e: e + 1 >= s)


if __name__ == '__main__':
    print(first())
    print(second())
