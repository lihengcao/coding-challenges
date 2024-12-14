from functools import reduce
from typing import Optional

def read_input():
    robots = []
    M, N = 0, 0
    while True:
        try:
            line = input()

            ps, vs = line.split(' ')

            # problem statement has x, y reversed, but probably doens't matter
            px, py = (int(n) for n in ps.split('=')[1].split(','))
            vx, vy = (int(n) for n in vs.split('=')[1].split(','))

            robots.append(((px, py), (vx, vy)))

            M = max(M, px)
            N = max(N, py)

        except EOFError:
            break

    return robots, M + 1, N + 1

def main():
    robots, M, N = read_input()

    print(calc_safety_factor(robots, M, N))

def calc_safety_factor(robots: list[tuple[tuple[int, int,], tuple[int, int]]], M: int, N: int) -> int:
    quadrants = [0] * 5

    for robot in robots:
        x, y = simulate_position(robot, M, N, 100)

        if (q := calc_quadrant(x, y, M, N)) is not None:
            quadrants[q] += 1
        
    print(quadrants)
    quadrants.pop()
    return reduce(lambda a, b: a * b, quadrants, 1)


def simulate_position(robot: tuple[tuple[int, int], tuple[int, int]], M: int, N: int, steps: int) -> tuple[int, int]:
    (x, y), (vx, vy) = robot

    final_x, final_y = x + vx * steps, y + vy * steps

    fitted_x, fitted_y = final_x % M, final_y % N

    return fitted_x, fitted_y


def calc_quadrant(x: int, y: int, M: int, N: int) -> Optional[int]:
    mid_x, mid_y = M//2, N//2 

    if x == mid_x or y == mid_y:
        return None

    row, col = 0, 0
    if x > mid_x:
        row = 1
    if y > mid_y:
        col = 1

    return row + col * 2
    


if __name__ == "__main__":
    main()
