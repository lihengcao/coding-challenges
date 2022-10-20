# largest prime factor

import math

number = 600_851_475_143 # underscore for visibility

def findPrime(n: int) -> int:
    if n & 1 == 0:
        # check if even
        return False

    # only check odds up to the square root
    for i in range(3, int(math.sqrt(n)), 2):
        if n % i == 0:
            return False

    return True

def findFactors(n: int) -> list[int]:
    res = [1]
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            res.append(i)

    for i in range(len(res)-1, -1, -1):
        res.append(n // res[i])

    return res

print(max([e for e in findFactors(number) if findPrime(e)]))
