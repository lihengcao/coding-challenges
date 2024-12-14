from functools import reduce
from typing import Optional
from math import inf


FILENAME = "input.txt"

def read_input():
    with open(FILENAME, "r") as f:
        lines = f.readlines()

    robots = []
    M, N = 0, 0

    for line in lines:

        ps, vs = line.split(' ')

        # problem statement has x, y reversed, but probably doens't matter
        px, py = (int(n) for n in ps.split('=')[1].split(','))
        vx, vy = (int(n) for n in vs.split('=')[1].split(','))

        robots.append(((px, py), (vx, vy)))

        M = max(M, px)
        N = max(N, py)

    return robots, M + 1, N + 1

def main():
    robots, M, N = read_input()

    steps = 1
    safety_factor = inf
    while True:
        candidate_safety_factor, simulated = calc_safety_factor(robots, M, N, steps)

        if candidate_safety_factor < safety_factor:
            display_output(simulated, M, N)
            print(steps)

            safety_factor = candidate_safety_factor
        steps += 1

def calc_safety_factor(robots: list[tuple[tuple[int, int,], tuple[int, int]]], M: int, N: int, steps: int):
    quadrants = [0] * 5

    simulated = []

    for robot in robots:
        x, y = simulate_position(robot, M, N, steps)

        simulated.append((x, y))

        if (q := calc_quadrant(x, y, M, N)) is not None:
            quadrants[q] += 1


        
    quadrants.pop()
    return reduce(lambda a, b: a * b, quadrants, 1), simulated


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
    

def display_output(robots: list[tuple[tuple[int, int,], tuple[int, int]]], M: int, N: int) -> None:
    display = [[' '] * N for _ in range(M)]

    for x, y in robots:
        display[x][y] = '#'

    for i in range(len(display)):
        display[i] = "".join(display[i])

    print("\n".join(display))
    
    _ = input('press enter to continue')

if __name__ == "__main__":
    main()
