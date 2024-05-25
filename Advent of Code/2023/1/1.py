INPUT = "1.txt"
DEBUG = False


def day1() -> None:
    ans = 0
    with open(INPUT, "r") as f:
        lines = f.readlines()

        for line in lines:
            for c in line:
                if c.isdigit():
                    ans += 10 * int(c)
                    break

            for c in reversed(line):
                if c.isdigit():
                    ans += int(c)
                    break

    print(ans)


conversions: dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def conv_to_int(line: str, ind: int, beginning: bool) -> int:
    for text, num in conversions.items():
        n = len(text)
        start = ind - (0 if beginning else n - 1)

        if start + n - 1 >= len(line) or start < 0:
            continue

        for i in range(n):
            if line[start + i] != text[i]:
                break
        else:
            if DEBUG:
                print(f"conv: {line=}, {ind=}, {start=}, {num=}")

            return num

    return 0


def day2() -> None:
    ans = 0
    with open(INPUT, "r") as f:
        lines = f.read().splitlines()

        for line in lines:
            if DEBUG:
                print(line)
            for i, c in enumerate(line):
                if c.isdigit():
                    c = int(c)
                else:
                    c = conv_to_int(line, i, True)

                if c != 0:
                    if DEBUG:
                        print(c)
                    ans += 10 * c
                    break

            for i in range(len(line) - 1, -1, -1):
                c = line[i]

                if c.isdigit():
                    c = int(c)
                else:
                    c = conv_to_int(line, i, False)

                if c != 0:
                    if DEBUG:
                        print(c)
                    ans += c
                    break
            if DEBUG:
                print("---")

    print(ans)


day2()
