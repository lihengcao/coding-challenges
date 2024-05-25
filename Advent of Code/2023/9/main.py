from math import lcm

INPUT = "input.txt"
DEBUG = False

# INPUT = "sample.txt"
DEBUG = True


def extrapolate(vals: list[int], backwards=False) -> int:
    if not vals or all(v == 0 for v in vals):
        return 0

    diffs = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]

    if backwards:
        return vals[0] - extrapolate(diffs, True)

    return vals[-1] + extrapolate(diffs)


def p1() -> None:
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    sequences = [[int(e) for e in line.split(" ") if e != ""] for line in lines]

    if DEBUG:
        print(sequences)

    extrapolated_values = 0

    for seq in sequences:
        extrapolated_values += extrapolate(seq)

    print(extrapolated_values)


def p2() -> None:
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    sequences = [[int(e) for e in line.split(" ") if e != ""] for line in lines]

    if DEBUG:
        print(sequences)

    extrapolated_values = 0

    for seq in sequences:
        extrapolated_values += extrapolate(seq, True)

    print(extrapolated_values)


p2()
