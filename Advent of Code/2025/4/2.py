def main():
    grid: list[list[str]] = []

    while True:
        try:
            grid.append(list(input()))
        except EOFError:
            break

    M, N = len(grid), len(grid[0])

    adj = calc_adj(M, N, grid)

    total = 0
    # prev = 0

    while removable := get_removable(grid, adj):
        for i, j in removable:
            edit_adj(M, N, grid, adj, i, j, False)

        # print("diff", total - prev)
        # prev = total
        total += len(removable)

    print(total)


def get_removable(
    grid: list[list[str]],
    adj: list[list[int]],
) -> list[tuple[int, int]]:
    o: list[tuple[int, int]] = []

    for i, r in enumerate(adj):
        for j, c in enumerate(r):
            if c < 4 and grid[i][j] == "@":
                o.append((i, j))

    return o


def calc_adj(M: int, N: int, grid: list[list[str]]) -> list[list[int]]:
    adj = [[0] * N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            if grid[i][j] != "@":
                continue

            edit_adj(M, N, grid, adj, i, j, True)

    return adj


def edit_adj(
    M: int,
    N: int,
    grid: list[list[str]],
    adj: list[list[int]],
    i: int,
    j: int,
    add: bool,
) -> None:
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == dj == 0:
                continue
            x, y = i + di, j + dj

            if 0 <= x < M and 0 <= y < N:
                if add:
                    adj[x][y] += 1
                else:
                    adj[x][y] -= 1
    if not add:
        grid[i][j] = "x"


if __name__ == "__main__":
    main()
