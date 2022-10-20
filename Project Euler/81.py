# path sum: down and right

from math import inf

M = [None] * 80

with open("files/81.txt", "r") as f:
    # in theory not good to load everything into memory, but it works
    for i in range(80):
        l = f.readline()
        M[i] = [int(e) for e in l.split(',')]

cache = [[None] * 80 for _ in range(80)]
cache[-1][-1] = M[-1][-1]


def solve(i, j):
    if 80 <= i or 80 <= j:
        return inf

    if cache[i][j] is not None:
        return cache[i][j]

    cache[i][j] = M[i][j] + min(solve(i + 1, j), solve(i, j + 1))

    return cache[i][j]


print(solve(0, 0))
