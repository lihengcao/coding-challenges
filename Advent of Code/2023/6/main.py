from math import sqrt

INPUT = "input.txt"
DEBUG = False

# INPUT = "sample.txt"
# DEBUG = True

# def bsearch()


def distance_traveled(time_held: int, total_time: int) -> int:
    return (total_time - time_held) * time_held


def p1() -> None:
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    times = [int(e) for e in lines[0].split(":")[1].split(" ") if e != ""]
    distances = [int(e) for e in lines[1].split(":")[1].split(" ") if e != ""]

    ans = 1

    for time, distance in zip(times, distances):
        ways = sum(
            int(distance_traveled(time_held, time) > distance)
            for time_held in range(1, time)
        )
        ans *= ways

    print(ans)


def p2() -> None:
    with open(INPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    time = int("".join(e for e in lines[0].split(":")[1].split(" ") if e != ""))
    distance = int("".join(e for e in lines[1].split(":")[1].split(" ") if e != ""))

    # quadratic ax^2 + bx + c
    # beating the distance can be modelled with - time_held^2 + total_time * time_held  - distance
    a, b, c = -1, time, -distance

    offset = sqrt(b * b - 4 * a * c)

    left_sol, right_sol = sorted([(-b - offset) / 2 * a, (-b + offset) / 2 * a])

    left_boundary, right_boundary = int(left_sol + 0.5), int(right_sol - 0.5)

    print(right_boundary - left_boundary)


p2()
