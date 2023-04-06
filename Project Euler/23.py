# Non-abundant sums

import math

def sum_factors(n: int) -> int:
    s = int(math.sqrt(n))
    ans = 1 + s if n == s * s else 1

    for d in range(2, int(s)):
        if n % d == 0:
            ans += d + n//d

    return ans

sums = [False] * (28123 + 1)

for i in range(2, len(sums)):
    sums[i] = True if sum_factors(i) > i else False
    if i % 500 == 0:
        print("sums", i)
        
ans = 0

for i, n in enumerate(sums):
    if i % 500 == 0:
        print("ans", i)
    if n is None or n == i:
        continue

    if n < len(sums) and sums[n] == i:
        ans += sums[n] + n
        sums[n] = None



print(ans)
