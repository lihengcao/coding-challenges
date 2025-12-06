def main():
    ranges: list[tuple[int, int]] = []

    for a in input().split(","):
        x, y = a.split("-")
        ranges.append((int(x), int(y)))
    ranges.sort()

    # print(ranges)

    cur = 1
    mul = 11
    div_check = 10
    count = 0

    for a, b in ranges:
        while (candidate := cur * mul) <= b:
            if candidate >= a:
                print(cur, mul, candidate)
                count += candidate

            cur += 1

            if cur // div_check != 0:
                mul = 10 * mul - 9
                div_check *= 10

    print(count)


if __name__ == "__main__":
    main()
