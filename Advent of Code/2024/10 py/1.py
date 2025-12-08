def read_input():
    grid = []
    while True:
        try:
            line = [int(e) for e in input()]

            grid.append(line)

        except EOFError:
            break

    return grid


def main():
    grid = read_input()

    print(calc_total_score(grid))


# no premature optimization!!
def calc_total_score(grid: list[list[int]]) -> int:
    M, N = len(grid), len(grid[0])

    starts = [(r, c) for r in range(M) for c in range(N) if grid[r][c] == 0]

    score = 0

    for start in starts:
        score += calc_score(grid, M, N, start)

    return score


DIRECTIONS = (
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
)


def calc_score(grid, M, N, start) -> int:
    visited = set()
    score = 0
    s = [start]

    while s:
        x, y = s.pop()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if grid[x][y] == 9:
            score += 1
            continue

        for dx, dy in DIRECTIONS:
            i, j = x + dx, y + dy

            if 0 <= i < M and 0 <= j < N and grid[i][j] == grid[x][y] + 1:
                s.append((i, j))

    return score


if __name__ == "__main__":
    main()
