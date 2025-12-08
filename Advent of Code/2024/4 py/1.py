def main():
    grid: list[str] = []

    while True:
        try:
            grid.append(input())
        except EOFError:
            break

    print(grid)
    M, N = len(grid), len(grid[0])
    WORD = "XMAS"

    xmas_count = 0

    for r in range(M):
        for c in range(N):
            if grid[r][c] != WORD[0]:
                continue

            xmas_count += search(grid, r, c, WORD, M, N)

    print(xmas_count)


def search(grid: list[str], r: int, c: int, WORD: str, M: int, N: int) -> int:
    occurs = 0

    # d{r | c} := delta {r | c}
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == dc == 0:
                continue

            i, j = r + dr, c + dc

            matched_word = [grid[r][c]]

            for char_i in range(1, len(WORD)):
                if not (0 <= i < M and 0 <= j < N and grid[i][j] == WORD[char_i]):
                    break

                matched_word.append(grid[i][j])
                i += dr
                j += dc
            else:
                print(r, c, dr, dc, "".join(matched_word))
                occurs += 1

    return occurs


if __name__ == "__main__":
    main()
