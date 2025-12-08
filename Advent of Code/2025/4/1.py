def main():
    grid: list[str] = []

    while True:
        try:
            grid.append(input())
        except EOFError:
            break

    M, N = len(grid), len(grid[0])

    adj = [[0] * N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            if grid[i][j] != "@":
                continue

            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == dj == 0:
                        continue
                    x, y = i + di, j + dj

                    if 0 <= x < M and 0 <= y < N:
                        adj[x][y] += 1

    # [print([c if c < 4 else 0 for c in r]) for r in adj]
    total = sum(
        sum(1 if c < 4 and grid[i][j] == "@" else 0 for j, c in enumerate(r))
        for i, r in enumerate(adj)
    )

    print(total)


if __name__ == "__main__":
    main()
