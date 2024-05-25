import math


def factors(n: int) -> int:
    s = int(math.sqrt(n))
    ans = 3 if n == s * s else 2

    for d in range(2, int(s)):
        if n % d == 0:
            ans += 2

    return ans


t, n = 2, 1  # triangle, number
best = 0
while True:
    f = factors(n)

    n += t
    t += 1

    best = max(best, f)
    print(t, n, f, best)

    if f > 500:
        break

print(n)
