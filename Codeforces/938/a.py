for _ in range(int(input())):
    n, a, b = [int(e) for e in input().split(" ")]

    if n % 2 == 0:
        print(min(n // 2 * b, n * a))
    else:
        print(min(n // 2 * b + a, n * a))
