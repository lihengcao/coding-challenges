# smallest multiple

from functools import reduce

up_to: int = 20

def primeFactors(n: int)-> dict[int, int]:
    ans: dict[int, int] = {}
    i: int = 2
    while n > 1:
        if n % i == 0:
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
            n //= i
        else:
            i += 1
    return ans

def combine(d1: dict[int, int], d2: dict[int,int])-> dict[int,int]:
    if len(d2) > len(d1):
        # invariant: d1 has more entries than d2
        d1, d2 = d2, d1
    for k, v in d2.items():
        if k not in d1:
            d1[k] = v
        elif v > d1[k]:
            d1[k] = v
    return d1

def multiply(d: dict[int, int])-> int:
    ans = 1
    for k, v in d.items():
        ans *= k**v

    return ans

factors: dict[int, int] = {}

for i in range(1, 21):
    factors = combine(factors, primeFactors(i))

print(multiply(factors))
