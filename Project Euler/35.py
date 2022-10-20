# circular primes below U

U = 1_000_000 + 1  # Upper bound

primes = [True] * U  # sieve
primes[0] = primes[1] = False

for i in range(2, len(primes)):
    for j in range(2 * i, len(primes), i):
        primes[j] = False
ans = 1


def rotate(n):
    s = list(str(n))
    se = set()

    candidates = []

    for _ in s:
        if (a := int(''.join(s))) not in se:
            candidates.append(a)
            se.add(a)
        s = s[1:] + s[:1]

    return candidates, len(se)


for i in range(3, len(primes), 2):
    if not primes[i]:
        continue

    r = rotate(i)

    for p in r[0]:
        if not primes[p]:
            break

        primes[p] = False  # looked at this already
    else:
        ans += r[1]

print(ans)
