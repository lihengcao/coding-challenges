def main():
    tiles: list[tuple[int, int]] = []

    while True:
        try:
            a, b = [int(e) for e in input().split(',')]
            tiles.append((a, b))
        except EOFError:
            break
    
    
    best = 0
    for i in range(len(tiles) - 1):
        for j in range(i + 1, len(tiles)):
            (a, b), (x, y) = tiles[i], tiles[j]

            cur = (abs(a - x) + 1) * (abs(b - y) + 1)

            best = max(best, cur)

    print(best)


if __name__ == "__main__":
    main()
