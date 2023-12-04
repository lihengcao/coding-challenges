# particle simulator

from my_code import *


filename = "input.txt"
# filename = "sample.txt"


with open(filename, "r") as f:
    rocks = [[[int(n) for n in rock.split(',')] for rock in line.strip().split(' -> ')] for line in f.readlines()]


def first() -> int:
    c = Cave(rocks)
    r = c.add_until_no_more()
    c.visualize()
    return r


def second() -> int:
    c = Cave(rocks, floor = True)
    r = c.add_until_no_more() + 1  # too hard to fix... just add one
    c.visualize()
    return r


if __name__ == '__main__':
    print(first())
    print(second())
