def read_input():
    grid = []
    while True:
        try:
            line = [-1 if e == '.' else int(e) for e in input()]

            grid.append(line)

        except EOFError:
            break

    return grid

def main():
    grid = read_input()

    print(calc_total_score(grid))

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

# I will admit, I did not try if a more brute force solution worked; I did a medium-mature optimization
def calc_score(grid, M, N, start) -> int:
    cache = {}

    def search(x, y) -> int:
        if (x, y) in cache:
            return cache[(x, y)]

        if grid[x][y] == 9:
            cache[(x, y)] = 1
            return 1
        
        score = 0
        
        for dx, dy in DIRECTIONS:
            i, j = x + dx, y + dy

            if 0 <= i < M and 0 <= j < N and grid[i][j] == grid[x][y] + 1:
                score += search(i, j)

        cache[(x, y)] = score
        return score

    x, y = start
    return search(x, y)



if __name__ == "__main__":
    main()
