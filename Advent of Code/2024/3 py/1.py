from enum import Enum


class LookingFor(Enum):
    MUL_LEFT = 0
    NUM1 = 1
    COMMA = 2
    NUM2 = 3
    RIGHT = 4


def main():
    total = 0
    state = LookingFor.MUL_LEFT

    while True:
        try:
            line = input()
            ind = 0
            num1, num2 = None, None

            while ind < len(line):
                match state:
                    case LookingFor.MUL_LEFT:
                        if line[ind : ind + len("mul(")] == "mul(":
                            state = LookingFor.NUM1
                            ind += len("mul(")
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
                            state = LookingFor.MUL_LEFT

                        ind += len(num)
                    case LookingFor.COMMA:
                        if line[ind] == ",":
                            state = LookingFor.NUM2
                        else:
                            state = LookingFor.MUL_LEFT

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
                            state = LookingFor.MUL_LEFT

                        ind += len(num)
                    case LookingFor.RIGHT:
                        if line[ind] == ")":
                            total += num1 * num2

                        state = LookingFor.MUL_LEFT
                        ind += 1

        except EOFError:
            break

    print(total)


if __name__ == "__main__":
    main()
