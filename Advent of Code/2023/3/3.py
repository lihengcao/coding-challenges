INPUT = "i.txt"
# INPUT = "s.txt"  # sample
DEBUG = False


def check_is_symbol(lines: list[str], i: int, j: int) -> bool:
    m, n = len(lines), len(lines[0])
    if not (0 <= i < m and 0 <= j < n):
        return False
    
    c = lines[i][j]
    return not (c.isdigit and c == '.')


def maybe_get_num(lines: list[str], i: int, j: int) -> int:
    # check left
    num = 0
    n = len(lines[0])
    symbol_adjacent = check_is_symbol(lines, i - 1, j - 1) or check_is_symbol(lines, i, j - 1) or check_is_symbol(lines, i + 1, j - 1)

    ind = j

    # check above and below
    while ind < n and (c := lines[i][ind]).isdigit():
        num = 10 * num + int(c)

        if not symbol_adjacent:
            symbol_adjacent = check_is_symbol(lines, i - 1, ind) or check_is_symbol(lines, i + 1, ind)

        ind += 1

    # check right
    if not symbol_adjacent:
            symbol_adjacent = check_is_symbol(lines, i - 1, ind) or check_is_symbol(lines, i, ind) or check_is_symbol(lines, i + 1, ind)

    if DEBUG and symbol_adjacent:
        print(i, j, num)

    return num if symbol_adjacent else 0


def p1() -> None:
    ans = 0
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

        for i, line in enumerate(lines):
            prev_was_digit = False
            for j, char in enumerate(line):
                if not char.isdigit():
                    prev_was_digit = False
                    continue

                if prev_was_digit:
                    continue

                prev_was_digit = True

                ans += maybe_get_num(lines, i, j)

    print(ans)


ADJACENT = (
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1)
)


def maybe_get_gear_ratio(lines: list[str], i: int, j: int) -> int:
    m, n = len(lines), len(lines[0])

    def parse_num(tup: tuple[int, int]) -> int:
        di, dj = tup
        x, y = i + di, j + dj
        l, r = y - 1, y + 1

        while l >= 0 and lines[x][l].isdigit():
            l -= 1

        while r < n and lines[x][r].isdigit():
            r += 1

        num = 0
        for k in range(l + 1, r):
            num = 10 * num + int(lines[x][k])

        return num


    candidates = set()
    for di, dj in ADJACENT:
        x, y = i + di, j + dj
        if not (0 <= x < m and 0 <= y < n and lines[x][y].isdigit()):
            continue
        candidates.add((di, dj))

    processed = []
    for candidate in candidates:
        di, dj = candidate

        if (di, dj - 1) in candidates:
            continue

        processed.append(candidate)

    if DEBUG:
        print(f"{candidates=}, {processed=}")

    if len(processed) != 2:
        return 0

    if DEBUG:
        print(processed)

    g1, g2 = parse_num(processed[0]), parse_num(processed[1])

    return g1 * g2


def p2() -> None:
    ans = 0
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if not char == '*':
                    continue

                ans += maybe_get_gear_ratio(lines, i, j)

    print(ans)


p2()
