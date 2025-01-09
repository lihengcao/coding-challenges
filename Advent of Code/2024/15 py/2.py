FILENAME = "s.txt"

DOUBLE_WIDE = {
    "#": ['#'] * 2,
    'O': ['[', ']'],
    '.': ['.'] * 2,
    '@': ['@', '.'],
}

def read_input():
    with open(FILENAME, "r") as f:
        lines = f.read().splitlines()

    grid = []
    instructions = []

    state_read_grid = True

    for line in lines:
        if line == "":
            state_read_grid = False
            continue

        if state_read_grid:
            grid.append([])
            for c in line:
                grid[-1].extend(DOUBLE_WIDE[c])
        else:
            instructions.extend(list(line))

    return grid, "".join(instructions)

def main():
    grid, instructions = read_input()
    # instructions = compress_instructions(instructions)

    print(calc_coordinate_sum(grid, instructions))
    
def calc_coordinate_sum(grid: list[list[str]], instructions: str) -> int:
    display_grid(grid)

    simulate_moves(grid, instructions)

    display_grid(grid)

    coordinate_sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                coordinate_sum += 100 * i + j

    return coordinate_sum

DIRECTIONS = {
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0),
}

def simulate_moves(grid: list[list[str]], instructions) -> None:
    rx, ry = find_robot(grid)

    for instruc in instructions:
        dx, dy = DIRECTIONS[instruc]
        try_move(grid, rx, ry, dx, dy)


def try_move(grid, x, y, dx, dy):
    

    x, y = rx + dx, ry + dy

    while grid[x][y] not in '.#':
        x, y = x + dx, y + dy
    print(x, y)
    if grid[x][y] == '#':
        continue

    grid[x][y] = 'O'
    grid[rx][ry] = '.'
    rx, ry = rx + dx, ry + dy

    grid[rx][ry] = '@'
        

def find_robot(grid) -> tuple[int, int]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                return i, j

    raise ValueError("can't find '@'; probably bad input")


def display_grid(grid) -> None:
    [print("".join(line)) for line in grid]

if __name__ == "__main__":
    main()
