def main():
    grid: list[str] = []

    while True:
        try:
            grid.append(input())
        except EOFError:
            break

    beams = set([find_start(grid)])
    splits = 0

    M, N = len(grid), len(grid[0])

    while beams:
        new: set[tuple[int, int]] = set()

        for r, c in beams:
            r += 1
            if r >= M:
                continue

            if grid[r][c] != "^":
                new.add((r, c))
                continue

            splits += 1

            if c - 1 >= 0:
                new.add((r, c - 1))
            if c + 1 < N:
                new.add((r, c + 1))

        beams = new

    print(splits)


def find_start(grid: list[str]) -> tuple[int, int]:
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                return r, c

    return -1, -1


if __name__ == "__main__":
    main()
