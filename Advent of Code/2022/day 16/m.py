# volcano valves
from collections import deque
from functools import cache


filename = "input.txt"
# filename = "sample.txt"

arr = []
with open(filename, "r") as f:
    for line in f.readlines():
        l = line.strip().split(' ')
        arr.append([l[1], int(l[4].split('=')[-1][:-1]), set([s[:-1] for s in l[9:-1]] + [l[-1]])])

rates = {r[0]: r[1] for r in arr}
nonzero_valves = frozenset([r[0] for r in arr if r[1] != 0] + ['AA'])
all_tunnels = {r[0]: r[2] for r in arr}

def distance(start: str, target: str) -> int:
    steps = 0
    q = deque([start])
    visited = set()

    while q:
        new = deque()

        while q:
            c = q.popleft()

            if c in target and c != start:
                return steps

            if c in visited:
                continue
            visited.add(c)

            for edge in all_tunnels[c]:
                new.append(edge)

        steps += 1
        q = new

    return steps

edges = {k: {vk: distance(k, vk) for vk in nonzero_valves if vk != k} for k in nonzero_valves}

@cache
def dfs1(valve: str='AA', time: int=30 + 1, pressure: int=0, visited: frozenset[str]=frozenset(('AA',))) -> int:
    if time <= 0:
        return pressure

    pressure += (time - 1) * rates[valve]

    if len(visited) + 1 == len(nonzero_valves):
        return pressure

    new_visited = visited | frozenset((valve,))
    not_visited = nonzero_valves - new_visited
    
    return max(dfs1(new_valve, time - edges[valve][new_valve] - 1, pressure, new_visited) for new_valve in not_visited)


def first() -> int:
    return dfs1()


def second() -> int:
    return 0


if __name__ == '__main__':
    print("first", first())
    print("second", second())
