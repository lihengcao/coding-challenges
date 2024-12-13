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

                machines[-1].append((x, y))

            
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

    max_A = max(Px//Ax, Py//Ay) + 1
    print(max_A)

    for A_presses in range(max_A):
        x, y = A_presses * Ax, A_presses * Ay

        need_x, need_y = Px - x, Py - y
        
        B_presses = need_x//Bx

        if need_x % Bx == 0 and By * B_presses == need_y:
            print(A_presses * 3 + B_presses, machine)
            return A_presses * 3 + B_presses

    print("inf", machine)
    return 0


if __name__ == "__main__":
    main()
