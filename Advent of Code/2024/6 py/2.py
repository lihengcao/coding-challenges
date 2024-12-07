def main():
    obstacles = set()
    start = None

    M, N = None, None

    row = 0
    while True:
        try:
            line = input()

            for col in range(len(line)):
                if line[col] == "^":
                    start = row, col
                elif line[col] == "#":
                    obstacles.add((row, col))

            N = len(line)
            row += 1
        except EOFError:
            break
    M = row

    print(count_obstacle_candidates(obstacles, start, M, N))


DIRECTIONS = (
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
)

def count_obstacle_candidates(obstacles, start, M, N) -> int:
    patroled = get_patroled(obstacles, start, M, N)
    count = 0

    for x, y in patroled:
        if (x, y) == start:
            continue

        obstacles.add((x, y))
        if check_loop(obstacles, start, M, N):
            count += 1
        obstacles.remove((x, y))

    return count


def get_patroled(obstacles: set[tuple[int, int]], start: tuple[int, int], M: int, N: int) -> int:
    visited = set([start])

    x, y = start
    direction_i = 0

    while 0 <= x < M and 0 <= y < N:
        if (x, y) in obstacles:
            dx, dy = DIRECTIONS[direction_i]
            x, y = x - dx, y - dy
            direction_i = (direction_i + 1) % len(DIRECTIONS)
            continue
    
        visited.add((x, y))

        dx, dy = DIRECTIONS[direction_i]
        x, y = x + dx, y + dy

    return visited

def check_loop(obstacles: set[tuple[int, int]], start: tuple[int, int], M: int, N: int) -> int:
    x, y = start
    direction_i = 0

    visited = set()

    while 0 <= x < M and 0 <= y < N:
        if (x, y) in obstacles:
            dx, dy = DIRECTIONS[direction_i]
            x, y = x - dx, y - dy
            direction_i = (direction_i + 1) % len(DIRECTIONS)
            continue

        pos = (x, y, direction_i)

        if pos in visited:
            return True

        visited.add(pos)

        dx, dy = DIRECTIONS[direction_i]
        x, y = x + dx, y + dy

    return False


if __name__ == "__main__":
    main()
