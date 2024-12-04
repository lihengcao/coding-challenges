from enum import Enum

class LookingFor(Enum):
    DONT_OR_MUL_LEFT = 0
    NUM1 = 1
    COMMA = 2
    NUM2 = 3
    RIGHT = 4
    DO = 5

def main():
    total = 0
    state = LookingFor.DONT_OR_MUL_LEFT

    while True:
        try:
            line = input()
            ind = 0
            num1, num2 = None, None

            while ind < len(line):
                # print(state, line[ind:ind + 8])
                match state:
                    case LookingFor.DONT_OR_MUL_LEFT:
                        if line[ind:ind + len("mul(")] == "mul(":
                            state = LookingFor.NUM1
                            ind += len("mul(")
                        elif line[ind:ind + len("don't()")] == "don't()":
                            state = LookingFor.DO
                            ind += len("don't()")
                        else:
                            ind += 1
                    case LookingFor.DO:
                        if line[ind:ind + len("do()")] == "do()":
                            state = LookingFor.DONT_OR_MUL_LEFT
                            ind += len("do()")
                        else:
                            ind += 1
                    case LookingFor.NUM1:
                        num = []
                        for j in range(3):
                            if line[ind + j].isnumeric():
                                num.append(line[ind + j])
                            else:
                                break

                        if 1 <= len(num) <= 3:
                            num1 = int("".join(num))
                            state = LookingFor.COMMA
                        else:
                            state = LookingFor.DONT_OR_MUL_LEFT

                        ind += len(num)
                    case LookingFor.COMMA:
                        if line[ind] == ",":
                            state = LookingFor.NUM2
                        else:
                            state = LookingFor.DONT_OR_MUL_LEFT
                        
                        ind += 1
                    case LookingFor.NUM2:
                        num = []
                        for j in range(3):
                            if line[ind + j].isnumeric():
                                num.append(line[ind + j])
                            else:
                                break

                        if 1 <= len(num) <= 3:
                            num2 = int("".join(num))
                            state = LookingFor.RIGHT
                        else:
                            state = LookingFor.DONT_OR_MUL_LEFT
                        
                        ind += len(num)
                    case LookingFor.RIGHT:
                        if line[ind] == ")":
                            total += num1 * num2

                        state = LookingFor.DONT_OR_MUL_LEFT
                        ind += 1

        except EOFError:
            break

    print(total)

if __name__ == "__main__":
    main()
