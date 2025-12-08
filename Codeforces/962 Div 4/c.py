for _ in range(int(input())):
    n, s, m = map(int, input().split(" "))

    intervals = [(0, 0), (m, m)]

    for _ in range(n):

        intervals.append(tuple(map(int, input().split(" "))))

    intervals.sort()

    for i in range(len(intervals) - 1):
        a, b = intervals[i][1], intervals[i + 1][0]
        if b - a >= s:
            print("YES")
            break
    else:
        print("NO")
