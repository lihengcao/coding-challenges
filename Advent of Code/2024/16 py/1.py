from heapq import heappop, heappush

FILENAME = "i.txt"

def read_input():
    with open(FILENAME, "r") as f:
        grid = f.read().splitlines()

    return grid


def find_in_grid(grid, target):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == target:
                return i, j

    raise Exception("can't find")
    

def main():
    grid = read_input()
    S = find_in_grid(grid, "S")
    E = find_in_grid(grid, "E")

    print(solve_maze(grid, S, E))

DIRECTIONS = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
)


def solve_maze(grid, S, E) -> int:
    heap = [(0, *S, 0)]

    visited = set()

    while heap:
        score, x, y, direc = heappop(heap)

        if grid[x][y] == '#' or (x, y, direc) in visited:
            continue

        if (x, y) == E:
            return score

        visited.add((x, y, direc))
        
        dx, dy = DIRECTIONS[direc]

        heappush(heap, (score + 1, x + dx, y + dy, direc))

        for dd in (-1, 1):
            heappush(heap, (score + 1000, x, y, (direc + dd) % 4))

        


    raise Exception("can't reach end")



if __name__ == "__main__":
    main()
