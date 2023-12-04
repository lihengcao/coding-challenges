# treehouse 

from math import inf


day = 8
filename = f"{day}.txt"
# filename = f"{day}s.txt"


def first() -> int:   
    with open(filename, "r") as f:
        grid = [[int(n) for n in l.strip()] for l in f.readlines()]

    m, n = len(grid), len(grid[0])
    visible = set()
    
    for startx, starty, endx, endy, dx, dy in ((0, 0, m, n, 1, 1), (m - 1, n - 1, -1, -1, -1, -1),):
        

        for i in range(startx, endx, dx):
            tallest = -inf
            for j in range(starty, endy, dy):
                if grid[i][j] > tallest:
                    visible.add((i, j,))
                    tallest = grid[i][j]

                pass
                
        
        for j in range(starty, endy, dy):
            tallest = -inf
            for i in range(startx, endx, dx):
                if grid[i][j] > tallest:
                    visible.add((i, j,))
                    tallest = grid[i][j]

    return len(visible)

def second() -> int:
    with open(filename, "r") as f:
        grid = [[int(n) for n in l.strip()] for l in f.readlines()]

    m, n = len(grid), len(grid[0])
    score = 0
    for x in range(m):
        for y in range(n):
            cur = 1

            for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1),):
                direc = 0
                i, j = x + dx, y + dy

                while 0 <= i < m and 0 <= j < n:
                    if grid[x][y] > grid[i][j]:
                        direc += 1
                    elif grid[x][y] <= grid[i][j]:
                        direc += 1
                        break

                    i += dx
                    j += dy
                cur *= direc

            score = max(score, cur)

    return score


if __name__ == '__main__':
    print(first())
    print(second())
