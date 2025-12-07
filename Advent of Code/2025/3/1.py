def main():
    banks: list[list[int]] = []

    while True:
        try:
            line = input()
            line = list(line)
            banks.append([int(e) for e in line])
        except EOFError:
            break

    total = 0
    for bank in banks:
        best1 = 0

        ind = 0

        for i, n in enumerate(bank):
            if n > best1:
                best1 = n
                ind = i

        if ind == len(bank) - 1:
            best1, best2 = max(bank[:-1]), best1
        else:
            best2 = max(bank[ind + 1:])

        print(best1 * 10 + best2)

        total += 10 * best1 + best2

    print(total)


if __name__ == "__main__":
    main()
