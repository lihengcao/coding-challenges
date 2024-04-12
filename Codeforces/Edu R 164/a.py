for _ in range(int(input())):
    n, m, k = [int(e) for e in input().split(' ')]

    largest_count = n//m + (0 if n%m == 0 else 1)

    if n - largest_count > k:
        print("yes")
    else:
        print("no")
