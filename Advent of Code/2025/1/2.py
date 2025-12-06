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
        zeros += n // 100
        n %= 100

        left = 100 if p == 0 else p
        right = 100 - p

        if dir == "L":
            p -= n
        elif dir == "R":
            p += n
        else:
            raise ValueError

        # print(dir, n, p, left, right)
        if (dir == "L" and n >= left) or (dir == "R" and n >= right):
            # print('---', dir, n, p)
            zeros += 1

        p %= 100

    print(zeros)


if __name__ == "__main__":
    main()
