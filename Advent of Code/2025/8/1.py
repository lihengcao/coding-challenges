from heapq import heapify, heappop

def main():
    pos: list[tuple[int, int, int]] = []

    while True:
        try:
            a, b, c = [int(e) for e in input().split(',')]
            pos.append((a, b, c))
        except EOFError:
            break
    
    
    to_connect = 10 if len(pos) == 20 else 1000

    d_2 = calc_dist_squared(pos)

    groups = list(range(len(pos)))


    for _ in range(to_connect):
        _, i, j = heappop(d_2)

        union(groups, i, j)

    junctions: dict[int, int] = {}

    for i in range(len(groups)):
        a = find(groups, i)

        if a not in junctions:
            junctions[a] = 1
        else:
            junctions[a] += 1

    largest = sorted(junctions.items(), key=lambda t: -t[1])

    p = 1

    for i in range(3):
        p *= largest[i][1]

    print(p)


def find(groups: list[int], a: int) -> int:
    if groups[a] == a:
        return a
    
    r = find(groups, groups[a])
    groups[a] = r
    return r


def union(groups: list[int], a: int, b: int) -> None:
    a = find(groups, a)
    b = find(groups, b)

    if b > a:
        a, b, = b, a

    groups[b] = a



def calc_dist_squared(pos: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    out: list[tuple[int, int, int]] = []

    for i in range(len(pos) - 1):
        a = pos[i]
        for j in range(i + 1, len(pos)):
            b = pos[j]
            d = (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2
            out.append((d, i, j))

    heapify(out)
    return out

if __name__ == "__main__":
    main()
