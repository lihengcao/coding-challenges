# the following pattern seems to hold

# (a+b)^2 - (a^2 + b^2)
# = 2ab

# (a+b+c)^2 - (a^2 + b^2 + c^2)
# = 2ab + 2ac + 2bc

# (a+b+c+d)^2 - (a^2 + b^2 + c^2 + d^2)
# = 2(ab + ac + ad + bc + bd + cd)
# = 2 * (a*(b+c+d) + b*(c+d) + c*d)

def f(n: int) -> int:
    # t := table of cumulative sums
    # t[a] <- b+c+d
    # t[b] <- c+d; ...
    t = [0] * (n - 1)
    t[n - 2] = n  # "base" case
    for i in range(n - 3, -1, -1):  # fill out rest of the table
        t[i] = t[i + 1] + i + 2

    return sum([2 * (i + 1) * t[i] for i in range(len(t))])


# def f(n: int) -> int:
#     res: int = 0
#     for i in range(1, n):
#         for j in range(i + 1, n + 1):
#             res += 2 * i * j
#
#     return res

# def f(n):
#     return sum([i * i for i in range(1, n + 1)]) \
#            - pow(sum([i for i in range(1, n + 1)]), 2)


print(f(10), f(100))
