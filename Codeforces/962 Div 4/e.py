from math import log

for _ in range(int(input())):
    lo, hi = map(int, input().split(" "))

    count = 2 * (int(log(lo, 3)) + int(lo % 3 != 0))
    lo += 1

    for n in range(lo, hi + 1):
        count += int(log(n, 3)) + int(n % 3 != 0)

    print(count)
