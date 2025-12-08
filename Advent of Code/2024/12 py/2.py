def read_input():
    grid = []
    while True:
        try:
            grid.append(list(input()))

        except EOFError:
            break

    return grid


def main():
    grid = read_input()

    print(calc_score(grid))


def calc_score(grid: list[list[str]]) -> int:
    M, N = len(grid), len(grid[0])
    total_score = 0
    for i in range(M):
        for j in range(N):
            total_score += calc_individual_score(grid, M, N, i, j)

    return total_score


DIRECTIONS = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
)


def calc_individual_score(grid, M, N, i, j) -> int:
    current = grid[i][j]
    edges = set()

    if current is None:
        return 0

    visited = set()

    s = [(i, j)]

    while s:
        x, y = s.pop()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in DIRECTIONS:
            a, b = x + dx, y + dy

            if 0 <= a < M and 0 <= b < N and grid[a][b] == current:
                s.append((a, b))
            else:
                edges.add(Edge((a, b), (x, y)))

    for i, j in visited:
        grid[i][j] = None

    sides = count_sides(edges)

    print(current, sides)

    return len(visited) * sides


class Edge:
    def __init__(self, first, second):
        # first, second = sorted([first, second])

        self.first = first
        self.second = second

    def __hash__(self):
        return hash((self.first, self.second))

    def __repr__(self):
        return str((self.first, self.second))

    def __eq__(self, other):
        return self.first == other.first and self.second == other.second


def count_sides(edges: set[Edge]) -> int:
    count = 0

    while edges:
        edge = edges.pop()
        a, b = edge.first
        c, d = edge.second

        is_vertical_edge = a == c

        if is_vertical_edge:
            adj = d - b
            # trunk-ignore(bandit/B101)
            assert abs(adj) == 1, (a, b, c, d)
            dx, dy = 1, 0
        else:
            adj = c - a
            # trunk-ignore(bandit/B101)
            assert b == d and abs(adj) == 1, (a, b, c, d)
            dx, dy = 0, 1

        x, y = a, b
        while True:
            x += dx
            y += dy
            if is_vertical_edge:
                i, j = x, y + adj
            else:
                i, j = x + adj, y

            candidate_edge = Edge((x, y), (i, j))

            if candidate_edge not in edges:
                break
            edges.remove(candidate_edge)

        x, y = a, b

        while True:
            x -= dx
            y -= dy
            if is_vertical_edge:
                i, j = x, y + adj
            else:
                i, j = x + adj, y

            candidate_edge = Edge((x, y), (i, j))

            if candidate_edge not in edges:
                break
            edges.remove(candidate_edge)

        count += 1

    return count


if __name__ == "__main__":
    main()
