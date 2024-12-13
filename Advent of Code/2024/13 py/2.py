import numpy as np

OFFSET = 10000000000000

def read_input():
    machines = []
    while True:
        try: 
            machines.append([])
            for _ in range(3):
                line = input().split(': ')[1]
                commas = line.split(', ')

                x = int(commas[0][2:])
                y = int(commas[1][2:])

                machines[-1].append([x, y])

            for i in range(2):
                machines[-1][-1][i] += OFFSET

            
            _ = input()

        except EOFError:
            break

    return machines

def main():
    machines = read_input()

    tokens = 0

    for machine in machines:
        tokens += calc_tokens(machine)

    print(tokens)

def calc_tokens(machine: list[tuple[int, int]]) -> int:
    (Ax, Ay), (Bx, By), (Px, Py) = machine

    """
    A_press * Ax + B_press * Bx = Px
    A_press * Ay + B_press * By = Py


    Ix = J

    I: 2x2 = 
    [Ax Bx 
    Ay By]  

    x: 2x1 = 
    [A_press 
    B_press]

    J: 2x1 =
    [Px
    Py]

    x = solve(I, J)
    Ix = J
    """
    I = np.array([
        [Ax, Bx], 
        [Ay, By]
    ])
    J = np.array([
        [Px], 
        [Py]
    ])

    x = np.linalg.solve(I, J)

    A_press, B_press = np.round(x[0, 0]), np.round(x[1, 0])

    if abs(A_press * Ax + B_press * Bx - Px) < 1 and abs(A_press * Ay + B_press * By - Py) < 1:
        return int(3 * A_press + B_press)

    return 0


if __name__ == "__main__":
    main()
