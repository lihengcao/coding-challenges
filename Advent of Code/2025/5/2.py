def main():
    ranges: list[tuple[int, int]] = []

    while (i := input()) != "":
        a, b = [int(e) for e in i.split('-')]
        ranges.append((a, b))

    
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
    for a, b in fresh:
        total += b - a + 1

    print(total)

if __name__ == "__main__":
    main()
