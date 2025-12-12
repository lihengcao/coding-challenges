from typing import Iterable


def main():
    orig: list[tuple[int, int]] = []

    while True:
        try:
            a, b = [int(e) for e in input().split(",")]
            # reverse for visualization purposes
            orig.append((b, a))
        except EOFError:
            break

    no_border_comp, m, n = compress_coords_with_gap(orig)

    interior = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(-1, len(no_border_comp) - 1):
        (a, b), (x, y) = no_border_comp[i], no_border_comp[i + 1]

        for i in range(min(a, x), max(a, x) + 1):
            for j in range(min(b, y), max(b, y) + 1):
                interior[i][j] = 1

    # display(m, n, interior)
    # print()
    fill(interior)
    # display(m, n, interior)


    best = 0
    for i in range(len(orig) - 1):
        for j in range(i + 1, len(orig)):
            (a, b), (x, y) = orig[i], orig[j]

            cur = (abs(a - x) + 1) * (abs(b - y) + 1)

            if cur > best:
                if valid(no_border_comp, i, j, interior):
                    best = max(best, cur)

    print(best)


def display(m: int, n: int, points: Iterable[Iterable[int]]) -> None:
    d = [["."] * (n + 1) for _ in range(m + 1)]
    for i, r in enumerate(points):
        for j, c in enumerate(r):
            if c == 1:
                d[i][j] = "#"
            elif c == 2:
                d[i][j] = 'X'
    [print("".join(r)) for r in d]


def compress_coords_with_gap(inp: Iterable[tuple[int, int]]) -> tuple[list[tuple[int, int]], int, int]:
    rows: set[int] = set()
    cols: set[int] = set()

    for r, c in inp:
        rows.add(r)
        cols.add(c)

    inv_rows: dict[int, int] = {}
    inv_cols: dict[int, int] = {}

    for i, r in enumerate(sorted(rows)):
        inv_rows[r] = i
    for i, c in enumerate(sorted(cols)):
        inv_cols[c] = i

    return [(inv_rows[r] * 2, inv_cols[c] * 2) for r, c in inp], len(rows) * 2 - 2, len(cols) * 2 - 2


def fill(interior: list[list[int]]) -> None:
    M, N = len(interior), len(interior[0])
    a, b = find_first(interior)

    q = [(a, b)]

    while q:
        new: list[tuple[int, int]] = []

        for i, j in q:
            if interior[i][j] != 0:
                continue

            interior[i][j] = 2

            for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                x, y = i + di, j + dj

                if 0 <= x < M and 0 <= y < N and interior[x][y] == 0:
                    new.append((x, y))

        q = new
        


def find_first(interior: list[list[int]]) -> tuple[int, int]:
    for i in range(len(interior)):
        cont = 0
        for j in range(len(interior) - 1):
            cont += interior[i][j]

            if cont == 1 and interior[i][j] == 0:
                return i, j
            
    raise ValueError


def valid(comp: list[tuple[int, int]], i: int, j: int, inside: list[list[int]]) -> bool:
    (a, b), (x, y) = comp[i], comp[j]

    for q in range(min(a, x), max(a, x) + 1):
        for w in range(min(b, y), max(b, y) + 1):
            if inside[q][w] == 0:
                return False

    return True


if __name__ == "__main__":
    main()
