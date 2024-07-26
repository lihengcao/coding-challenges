from heapq import heappop, heappush, heapify

for _ in range(int(input())):
    n, k = map(int, input().split(' '))

    a = map(int, input().split(' '))
    b = map(int, input().split(' '))

    h = [(-x, y) for x, y in zip(a, b)]

    heapify(h)

    score = 0

    for _ in range(k):
        x, y = heappop(h)

        score -= x

        x = -max(0, -x - y)

        heappush(h, (x, y))

    print(score)


