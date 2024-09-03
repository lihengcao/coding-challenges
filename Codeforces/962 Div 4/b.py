for _ in range(int(input())):
    x = list(map(int, input().split(' ')))

    count = 0
    for i in (0, 1):
        for j in (0, 1):
            a, b, c, d = x[i], x[1 - i], x[2 + j], x[3 - j]

            count += int(
                (a > c and b >= d) or
                (a >= c and b > d)
            )


    # count = (
    #     int(a > c and b >= d) + 
    #     int(a > d and b >= c) + 
    #     int(b > c and a >= d) + 
    #     int(b > d and a >= c)
    #     )
    print(count)
    