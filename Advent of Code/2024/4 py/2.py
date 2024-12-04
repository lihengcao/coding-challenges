def main():
    grid: list[str] = []

    while True:
        try:
            grid.append(input())
        except EOFError:
            break

    print(grid)
    M, N = len(grid), len(grid[0])

    xmas_count = 0

    for r in range(1, M - 1):
        for c in range(1, N - 1):
            if grid[r][c] != "A":
                continue

            xmas_count += int(search(grid, r, c, M, N))
    
    print(xmas_count)

def search(grid: list[str], r: int, c: int, M: int, N: int) -> int:
    # forward / and back \ combine to make X

    forward = sorted([grid[r - 1][c + 1], grid[r + 1][c - 1]]) == ["M", "S"]
    backward = sorted([grid[r - 1][c - 1], grid[r + 1][c + 1]]) == ["M", "S"]

    return forward and backward



if __name__ == "__main__":
    main()
