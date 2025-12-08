for _ in range(int(input())):
    x, y, k = map(int, input().split(" "))

    x_m = x // k + int(x % k != 0)
    y_m = y // k + int(y % k != 0)

    x_m = (x_m - 1) * 2 + 1
    y_m *= 2

    print(max(x_m, y_m))
