from typing import Tuple


day = 9
filename = f"{day}.txt"
# filename = f"{day}s.txt"
# filename = f"{day}s2.txt"

with open(filename, "r") as f:
    motions = [l.strip().split(' ') for l in f.readlines()]

direction_to_delta = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}



def get_tail_position(hx: int, hy: int, tx: int, ty: int) -> Tuple[int, int]:
    if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:  # currently touching
        return tx, ty
    elif abs(hy - ty) == 2 and abs(hx - tx) == 2:  # one diagonal away
        return (hx + tx)//2, (hy + ty)//2
    elif hx == tx or abs(hy - ty) == 2 :  # same row
        return hx, (hy + ty)//2
    # else:
    elif hy == ty or abs(hx - tx) == 2:  # same column
        return (hx + tx)//2, hy


def visualize(rope, m=20, n=25) -> None:
    grid = [['.' for _ in range(n)] for _ in range(m)]

    for i in range(len(rope) - 1, -1, -1):
        marker = 'H' if i == 0 else str(i)
        x, y = rope[i][0], rope[i][1]

        grid[m//2 - y][n//2 + x] = marker

    [print(''.join(r)) for r in grid]
    print()


def first() -> int:   
    tail_visited = set()
    hx, hy, tx, ty = 0, 0, 0, 0

    for motion in motions:
        direction, times = motion
        dx, dy = direction_to_delta[direction]

        for time in range(int(times)):
            hx += dx
            hy += dy

            tx, ty = get_tail_position(hx, hy, tx, ty)

            tail_visited.add((tx, ty,))
            

    return len(tail_visited)


def second() -> int:
    tail_visited = set()
    rope = [(0, 0,) for _ in range(10)]

    for motion in motions:
        direction, times = motion
        dx, dy = direction_to_delta[direction]

        for time in range(int(times)):
            prevx, prevy = rope[0]
            rope[0] = rope[0][0] + dx, rope[0][1] + dy

            for i in range(1, len(rope)):
                new = get_tail_position(rope[i - 1][0], rope[i - 1][1], rope[i][0], rope[i][1])

                prevx, prevy = rope[i]

                rope[i] = new


            tail_visited.add(rope[-1])
            
            # print(direction, time) 
            # visualize(rope)
            

    return len(tail_visited)


if __name__ == '__main__':
    # print(first())
    print(second())
