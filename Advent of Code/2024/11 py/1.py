def read_input():
    return [s for s in input().split(" ") if s != ""]


def main():
    stones = read_input()

    print(blink(stones))


def blink(stones: list[str]) -> int:
    for i in range(25):
        new = []

        for stone in stones:
            if stone == "0":
                new.append("1")
            elif len(stone) % 2 == 0:
                N = len(stone) // 2
                left, right = stone[:N], stone[N:]
                right = str(int(right))
                new.extend([left, right])
            else:
                new.append(str(int(stone) * 2024))

        stones = new
        print(i, len(stones))

    return len(stones)


if __name__ == "__main__":
    main()
