def sum_from_to(f: int, t: int) -> int:
    n = t - f

    return n * f + n * (n - 1) // 2

    return d

# double check bounds
# assert sum_from_to(1, 2) == 1
# assert sum_from_to(1, 3) == 3


def minimize(k: int, m: int, end: int) -> int:
    left, right = sum_from_to(k, m), sum_from_to(m, end)

    return abs(left - right)




for _ in range(int(input())):
    n, k = map(int, input().split(' '))

    end = n + k

    lo, hi = n, end - 1

    # while lo < hi:
        # m = (lo + hi) // 2

        # a, b, c = 
    

    

