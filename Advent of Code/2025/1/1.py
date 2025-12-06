def main():
    zeros = 0

    ops = []

    while True:
        try:
            line = input()
            dir, n = line[0], int(line[1:])
            ops.append((dir, n))
        except EOFError:
            break

    p = 50

    for dir, n in ops:
        if dir == "L":
            p -= n
        elif dir == "R":
            p += n

        p %= 100

        if p == 0:
            zeros += 1

    print(zeros)


if __name__ == "__main__":
    main()
