from collections import defaultdict

def main():
    grid: list[str] = []

    while True:
        try:
            grid.append(input())
        except EOFError:
            break
    
    beams: defaultdict[tuple[int, int], int] = defaultdict(int)
    beams[*find_start(grid)] = 1
    splits = 0

    M, N = len(grid), len(grid[0])

    while beams:
        new: defaultdict[tuple[int, int], int] = defaultdict(int)

        for (r, c), count in beams.items():
            r += 1
            if r >= M:
                splits += count
                continue

            if grid[r][c] != "^":
                new[r, c] += count
                continue

            if c - 1 >= 0:
                new[r, c - 1] += count
            if c + 1 < N:
                new[r, c + 1] += count

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
