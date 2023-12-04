# 

from my_code import *


filename = "input.txt"
# filename = "sample.txt"


with open(filename, "r") as f:
    sensors_and_beacons: list[list[int]] = [[int(b.split('=')[-1]) for a in line.strip().split(':') for b in a.split(',')] for line in f.readlines()]


# [print(r) for r in sensors_and_beacons]


bounds = get_bounds(sensors_and_beacons)


def first() -> int:
    return count_cant_be_beacon(sensors_and_beacons, bounds, 10 if filename == "sample.txt" else 2_000_000)


def second() -> str:
    return "gg"


if __name__ == '__main__':
    print(first())
    print(second())
