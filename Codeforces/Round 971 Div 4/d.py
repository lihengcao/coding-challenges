for _ in range(int(input())):
    points = set()

    triangles = 0

    n = int(input())

    for _ in range(n):
        x, y = map(int, input().split(' '))
        points.add((x, y,))

        if (x, 1 - y) in points:
            triangles += n - 2

    for x, y in points:
        if (x - 1, 1 - y) in points and (x + 1, 1 - y) in points:
            triangles += 1
    
    print(triangles)