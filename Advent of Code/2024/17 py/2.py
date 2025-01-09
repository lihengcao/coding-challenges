FILENAME = "i.txt"

def read_input():
    with open(FILENAME, "r") as f:
        lines = f.read().splitlines()

    A = int(lines[0].split(': ')[1])
    B = int(lines[1].split(': ')[1])
    C = int(lines[2].split(': ')[1])
    program = [int(n) for n in lines[4].split(': ')[1].split(',')]

    return A, B, C, program

def main():
    A, B, C, program = read_input()

    combo = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: A,
        5: B,
        6: C,
    }

    output = []

    instruction_pointer = 0

    while instruction_pointer < len(program) - 1:
        instruc = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        # print(instruction_pointer, instruc, operand, combo[4], combo[5], combo[6])

        match instruc:
            case 0:
                combo[4] = combo[4] >> combo[operand]
            case 1:
                combo[5] = combo[5] ^ operand
            case 2:
                combo[5] = combo[operand] % 8
            case 3:
                if combo[4] != 0:
                    instruction_pointer = operand - 2
            case 4:
                combo[5] = combo[5] ^ combo[6]
            case 5:
                output.append(str(combo[operand] % 8))
            case 6:
                combo[5] = combo[4] >> combo[operand]
            case 7:
                combo[6] = combo[4] >> combo[operand]

        instruction_pointer += 2

    print('---')
    print(combo[4], combo[5], combo[6])
    print(",".join(output))



if __name__ == "__main__":
    main()
