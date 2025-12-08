from collections import defaultdict
from math import log10


def read_input():
    return [int(s) for s in input().split(" ") if s != ""]


def main():
    ordered_stones = read_input()

    stones = defaultdict(int)

    for stone in ordered_stones:
        stones[stone] += 1

    print(blink(stones))


def blink(stones: dict[int, int]) -> int:
    for i in range(25):
        new = defaultdict(int)

        for stone, count in stones.items():
            if stone == 0:
                new[1] += count
            elif (N := count_digits(stone)) % 2 == 0:
                left, right = split_number(stone, N)

                new[left] += count
                new[right] += count
            else:
                new[stone * 2024] += count

        stones = new
        print(i, sum(stones.values()))

    return sum(stones.values())


def count_digits(n: int) -> int:
    return int(log10(n)) + 1


def split_number(n: int, length: int) -> tuple[int, int]:
    M = length // 2

    cutoff = 10**M

    left = n // cutoff
    right = n % cutoff

    return left, right


if __name__ == "__main__":
    main()
