for _ in range(int(input())):
    _ = input()
    a = [int(e) for e in input().split(' ')]

    l = 0  # makes an edge case easier
    while l < len(a) - 1:
        if a[l] != a[-1]:
            break
        l += 1

    if l == len(a) - 1:
        print(-1)
        continue

    r = len(a) - 2
    while r > 0:
        if a[r] != a[0]:
            break
        r -= 1

    print(min(l, len(a) - r - 1))

    print(f"{len(a) - r - 1=}")
