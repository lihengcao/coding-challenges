from heapq import *

def first():
    best = 0
    cur = 0
    with open("1.txt", "r") as f:
        for n in f.readlines():
            if n != '\n':
                cur += int(n)
            else:
                best = max(best, cur)
                cur = 0
    
    best = max(best, cur)
    print(best)

def second():
    ns = []
    cur = 0
    with open("1.txt", "r") as f:
        for n in f.readlines():
            if n != '\n':
                cur += int(n)
            else:
                ns.append(-cur)
                cur = 0

    heapify(ns)
    print(sum(-heappop(ns) for _ in range(3)))

first()
second()