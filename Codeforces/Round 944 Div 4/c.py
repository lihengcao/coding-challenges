"""Round 944"""
for _ in range(int(input())):
    order = [int(e) for e in input().split(' ')]
    a, b, c, d = order

    a, b = min(a, b), max(a, b)
    c, d = min(c, d), max(c, d)

    order.sort()

    if (order[0] == a and order[2] == b) or (order[0] == c and order[2] == d):
        print("yes")
    else:
        print("no")
