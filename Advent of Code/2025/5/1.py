def main():
    ranges: list[tuple[int, int]] = []
    ingredients: list[int] = []

    while (i := input()) != "":
        a, b = [int(e) for e in i.split("-")]
        ranges.append((a, b))

    while True:
        try:
            ingredients.append(int(input()))
        except EOFError:
            break

    ranges.sort()
    fresh: list[tuple[int, int]] = []

    for cur in ranges:
        if not fresh:
            fresh.append(cur)
            continue

        while fresh and cur[0] <= fresh[-1][1]:
            prev = fresh.pop()
            cur = (min(cur[0], prev[0]), max(cur[1], prev[1]))

        fresh.append(cur)

    total = 0
    for ing in ingredients:
        total += int(find(fresh, ing))

    print(total)


def find(fresh: list[tuple[int, int]], ing: int) -> bool:
    lo, hi = 0, len(fresh) - 1

    while lo < hi:
        m = (lo + hi) // 2
        if ing <= fresh[m][1]:
            hi = m
        else:
            lo = m + 1

    return fresh[lo][0] <= ing <= fresh[lo][1]


if __name__ == "__main__":
    main()
