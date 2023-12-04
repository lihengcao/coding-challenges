# screen


filename = "input.txt"
# filename = "sample.txt"

with open(filename, "r") as f:
    instructions = [l.strip().split(' ') for l in f.readlines()]


def first() -> int:
    reg = 1
    cycle = 1
    s = 0
    for ins in instructions:
        if (cycle - 20) % 40 == 0:
            s += cycle * reg

        if ins[0] == "addx":
            if (cycle - 20) % 40 == 39:
                s += (cycle + 1) * reg

            reg += int(ins[1])
            cycle += 2
        else:
            cycle += 1

    return s


def update_screen(screen: list[list[str]], cycle: int, reg: int) -> None:
    if abs(((cycle - 1) % 40) - reg) <= 1:
        screen[((cycle - 1)//40)][(cycle - 1) % 40] = '#'


def second(width: int=40, height: int=6) -> str:
    screen = [['.'] * width for _ in range(height)]
    reg = 1  # register value and sprite position
    cycle = 1
    for ins in instructions:
        update_screen(screen, cycle, reg)

        if ins[0] == "addx":
            cycle += 1
            update_screen(screen, cycle, reg)
            reg += int(ins[1])

        cycle += 1
    
    return '\n'.join([''.join(r) for r in screen])


if __name__ == '__main__':
    print(first())
    print(second())
