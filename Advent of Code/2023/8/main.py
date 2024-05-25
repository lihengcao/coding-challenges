from math import lcm

INPUT = "input.txt"
DEBUG = False

# INPUT = "sample.txt"
DEBUG = True


def p1() -> None:
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    LR = lines[0]
    start = "AAA"

    nodes: dict[str, tuple[str, str]] = {}
    for i in range(2, len(lines)):
        line = lines[i]

        l, r = [e.strip() for e in line.split("=")]

        r = tuple(s.lstrip() for s in r[1:-1].split(","))
        assert len(r) == 2

        nodes[l] = r

    cur = start
    steps = 0
    while cur != "ZZZ":
        ind = steps % len(LR)

        direction = 0 if LR[ind] == "L" else 1

        cur = nodes[cur][direction]

        steps += 1

    print(steps)


def traverse_cycle(
    nodes: dict[str, tuple[str, str]], LR: str, start: str
) -> dict[tuple[int, int], int]:
    cycle = {}
    steps = 1
    cur = nodes[start][0 if LR[0] == "L" else 1]
    while cur != start and cur[-1] != "A":
        ind = steps % len(LR)

        if cur[-1] == "Z":
            data = (cur, ind)
            if data in cycle:
                return cycle
            cycle[data] = steps

        direction = 0 if LR[ind] == "L" else 1

        cur = nodes[cur][direction]

        steps += 1

    return cycle


def p2() -> None:
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    LR = lines[0]
    starts = []

    nodes: dict[str, tuple[str, str]] = {}
    for i in range(2, len(lines)):
        line = lines[i]

        l, r = [e.strip() for e in line.split("=")]

        if l[-1] == "A":
            starts.append(l)

        r = tuple(s.lstrip() for s in r[1:-1].split(","))
        assert len(r) == 2

        nodes[l] = r

    cycles = [traverse_cycle(nodes, LR, start) for start in starts]
    if DEBUG:
        [print(c) for c in cycles]

    # did some offline data analysis, probably got lucky with my input
    # funnily enough, this wouldn't have worked with the sample without modifications, so very lucky indeed

    vals = [next(iter(c.values())) for c in cycles]

    print(lcm(*vals))


p2()
