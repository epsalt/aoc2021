import heapq

with open("input.txt") as inputs:
    lines = inputs.read().splitlines()
    matrix = []
    for line in lines:
        row = [int(num) for num in line]
        matrix.append(row)


def neighbours(cell, matrix):
    i, j = cell
    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
            yield x, y


def expand(matrix):
    r, c = len(matrix), len(matrix[0])

    out = []
    for i in range(r * 5):
        row = []
        for j in range(c * 5):
            extra = (i // r) + (j // c)
            new = matrix[i % r][j % c] + extra
            row.append((new - 1) % 9 + 1)
        out.append(row)

    return out


def dijkstra(start, matrix):
    dists = [[float("inf")] * len(row) for row in matrix]
    dists[start[0]][start[1]] = 0
    visited = set()

    q = []
    heapq.heappush(q, (0, start))

    while q:
        total, curr = heapq.heappop(q)
        visited.add(curr)

        for x, y in neighbours(curr, matrix):
            if (x, y) not in visited:
                dist = total + matrix[x][y]
                if dist < dists[x][y]:
                    dists[x][y] = dist
                    heapq.heappush(q, (dist, (x, y)))

    return dists[-1][-1]


def part1(matrix):
    return dijkstra((0, 0), matrix)


def part2(matrix):
    matrix = expand(matrix)
    return dijkstra((0, 0), matrix)
