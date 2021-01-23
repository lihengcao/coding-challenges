# Problem 7

from math import *


def is_prime(num: int) -> bool:
    for i in range(3, int(sqrt(num) + 1)):
        if num % i == 0:
            return False

    return True


c: int = 0  # c := counter
n: int = 3  # n := current number
while c != 10_000:  # compensate for starting count at 3 instead of 2
    if is_prime(n):
        c += 1
    n += 2

print(n - 2)
