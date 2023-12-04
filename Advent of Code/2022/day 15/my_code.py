# some code

from collections import defaultdict

from array import array


def get_manhattan_distance(ax: int, ay: int, bx: int, by: int) -> int:
    return abs(ax - bx) + abs(ay - by)


def get_bounds(sensors_and_beacons: list[list[int]]) -> tuple[int, int, int, int]:
    extremas = [[], []]

    for sx, sy, bx, by in sensors_and_beacons:
        mh = get_manhattan_distance(sx, sy, bx, by)

        extremas[0].extend([sx + mh, sx - mh])
        extremas[1].extend([sy + mh, sy - mh])

    min_x = min(extremas[0])
    max_x = max(extremas[0])

    # assume that target row is between min and max y
    min_y = min(extremas[1])
    max_y = max(extremas[1])

    return min_x, max_x, min_y, max_y


def count_cant_be_beacon(sensors_and_beacons: list[list[int]], bounds: tuple[int, int, int, int], target_y: int) -> int:  # kinda scuffed
    min_x, max_x, min_y, max_y = bounds

    if not (min_y <= target_y <= max_y):
        return -1

    row = defaultdict(lambda: '.')

    
    for sx, sy, bx, by in sensors_and_beacons:
        if by == target_y:
            row[bx] = 'B'
        elif sy == target_y:
            row[sx] = 'S'
        
        mh = get_manhattan_distance(sx, sy, bx, by)

        d = 0

        while get_manhattan_distance(sx + d, target_y, sx, sy) <= mh:
            for sign in (-1, 1,):
                x = sx + sign * d
                if row[x] == '.':
                    row[x] = '#'
            
            d += 1

    return sum(1 for x in range(min_x, max_x + 1) if row[x] == '#' or row[x] == 'S')


def search_for_beacon(sensors_and_beacons: list[list[int]], lower: int = 0, upper: int= 0) -> int:
    n = 4_000_000 + 1
    cave = array('b', )

    cave = [[False] * n for _ in range(n)]

    for sx, sy, bx, by in sensors_and_beacons:
                
        mh = get_manhattan_distance(sx, sy, bx, by)
        print(mh)
        # d = 0

        # while get_manhattan_distance(sx + d, target_y, sx, sy) <= mh:
        #     for sign in (-1, 1,):
        #         x = sx + sign * d
        #         if row[x] == '.':
        #             row[x] = '#'
            
        #     d += 1

    # for y in (range(lower, upper + 1)):
    #     print(y)

    #     if count_cant_be_beacon():
    #         pass
    x, y = 0, 0

    return 4000000 * x + y