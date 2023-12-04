# some functions
# definitely could've done this in less code and time, but this feels cleaner and is better organized
from enum import Enum


def sign(n: int) -> int:
    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1


class Material(Enum):
        SOURCE = '+'
        ROCK = '#'
        SAND = 'o'
        AIR = '.'


class Cave:
    def __init__(self, rock_lines: list[list[list[int]]], floor = False) -> None:
        self.materials = 0
        xs = [rock[0] for rock_line in rock_lines for rock in rock_line]
        ys = [rock[1] for rock_line in rock_lines for rock in rock_line]

        self.min_x = min(xs)
        self.max_x = max(xs)
        self.max_y = max(ys)

        # for more varied inputs, there needs to be a check to ensure that 500, 0 is in the cave
        m, n = self.max_y - 0 + 1, self.max_x - self.min_x + 1

        if floor:
            m += 2
            n = 2 * m  # definitely taller than wide, don't need to worry about n > 2 * m for these inputs
            self.min_x = 500 - m

        self.cave = [[Material.AIR] * n for _ in range(m)]
        self.add(Material.SOURCE, 500, 0)  # sand source

        for rock_line in rock_lines:
            for i_rock in range(len(rock_line) - 1):
                from_x, from_y = rock_line[i_rock]
                to_x, to_y = rock_line[i_rock + 1]

                dir_x, dir_y = sign(to_x - from_x), sign(to_y - from_y)

                while from_y != to_y or from_x != to_x:
                    self.add(Material.ROCK, from_x, from_y)

                    from_x += dir_x
                    from_y += dir_y

                self.add(Material.ROCK, to_x, to_y)

        if floor:
            self.cave[-1] = [Material.ROCK for _ in self.cave[0]]


    def adjust_coord(self, x: int) -> int:
        return x - self.min_x


    def add(self, mat: Material = Material.SAND, x: int = 500, y: int = 0) -> None:
        i, j = y, self.adjust_coord(x)

        if mat is Material.SAND:
            i, j = self.simulate(i, j)
            
        if mat is not Material.SAND or (0 < i < len(self.cave) - 1 and 0 <= j < len(self.cave[0])):
            self.cave[i][j] = mat
            if mat is Material.SAND:
                self.materials += 1
            


    def simulate(self, i: int, j: int) -> tuple[int, int]:
        while 0 <= i < len(self.cave) - 1 and 0 <= j < len(self.cave[0]):
            if Material.SAND is not self.cave[i + 1][j] is not Material.ROCK:
                i += 1
            elif j == 0 or Material.SAND is not self.cave[i + 1][j - 1] is not Material.ROCK:
                j -= 1
            elif j == len(self.cave[0]) - 1 or Material.SAND is not self.cave[i + 1][j + 1] is not Material.ROCK:
                j += 1
            else:
                break

        return i, j


    def add_until_no_more(self) -> int:
        before = self.materials

        while True:
            self.add() 
            if before == self.materials:
                return before
            before += 1


    def visualize(self) -> None:
        print('-' * len(self.cave[0]))
        print()
        for row in self.cave:
            print(''.join([e.value for e in row]))
        print()
        print('-' * len(self.cave[0]))
