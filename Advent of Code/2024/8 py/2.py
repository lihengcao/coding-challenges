from collections import defaultdict


def main():
    antennas = defaultdict(list)
    row = 0
    M, N = None, None
    while True:
        try:
            line = input()

            N = len(line)
            for col in range(len(line)):
                if line[col] == ".":
                    continue

                antennas[line[col]].append((row, col))

            row += 1

        except EOFError:
            break

    M = row

    print(count_antinodes(antennas, M, N))


def count_antinodes(antennas: dict[str, list[tuple[int, int]]], M, N) -> int:
    s = set()

    for locations in antennas.values():
        for ind1 in range(len(locations) - 1):
            for ind2 in range(ind1 + 1, len(locations)):
                a, b = locations[ind1]
                i, j = locations[ind2]

                s.add((a, b))
                s.add((i, j))

                d1, d2 = i - a, j - b

                x, y = i + d1, j + d2
                while 0 <= x < M and 0 <= y < N:
                    s.add((x, y))
                    x += d1
                    y += d2

                x, y = a - d1, b - d2
                while 0 <= x < M and 0 <= y < N:
                    s.add((x, y))
                    x -= d1
                    y -= d2

    return len(s)


if __name__ == "__main__":
    main()
