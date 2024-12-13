def read_input():
    grid = []
    while True:
        try:
            grid.append(list(input()))

        except EOFError:
            break

    return grid

def main():
    grid = read_input()

    print(calc_score(grid))


def calc_score(grid: list[list[str]]) -> int:
    M, N = len(grid), len(grid[0])
    total_score = 0
    for i in range(M):
        for j in range(N):
            total_score += calc_individual_score(grid, M, N, i, j)

    return total_score

DIRECTIONS = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
)

def calc_individual_score(grid, M, N, i, j) -> int:
    current = grid[i][j]
    perimeter = 0
    
    if current is None:
        return 0

    visited = set()

    s = [(i, j)]

    while s:
        x, y = s.pop()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in DIRECTIONS:
            a, b = x + dx, y + dy

            if 0 <= a < M and 0 <= b < N and grid[a][b] == current:
                s.append((a, b))
            else:
                perimeter += 1

    for i, j in visited:
        grid[i][j] = None

    return len(visited) * perimeter



if __name__ == "__main__":
    main()
