"""Round 944"""

from bisect import bisect_left


def calc(dists: list[int], times: list[int], query: int) -> int:
    ind = bisect_left(dists, query)

    if dists[ind] == query:
        return times[ind]

    dist = dists[ind] - dists[ind - 1]
    time = times[ind] - times[ind - 1]

    # speed = dist/time

    partial_dist = query - dists[ind - 1]

    # return times[ind - 1] + int(partial_dist/speed)

    # After the contest: looks like a rounding issue.
    # Maybe multiplying before dividing makes it more precise?

    # Wow. It was a rounding issue that could be solved by doing this:

    return times[ind - 1] + int(partial_dist * time / dist)


def main():
    for _ in range(int(input())):
        _, _, q = [int(e) for e in input().split(" ")]
        dists = [0] + [int(e) for e in input().split(" ")]
        times = [0] + [int(e) for e in input().split(" ")]

        for _ in range(q):
            query = int(input())
            print(calc(dists, times, query), end=" ")
        print()


if __name__ == "__main__":
    main()
