from math import prod

with open("input.txt") as inputs:
    lines = inputs.read().splitlines()
    matrix = []
    for line in lines:
        matrix.append([int(num) for num in line])


def neighbours(i, j, matrix):
    r, c = len(matrix), len(matrix[0])
    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if 0 <= x < r and 0 <= y < c:
            yield x, y


def lows(matrix):
    r, c = len(matrix), len(matrix[0])
    for i in range(r):
        for j in range(c):
            if all(matrix[i][j] < matrix[x][y] for x, y in neighbours(i, j, matrix)):
                yield i, j


def dfs(i, j, found, matrix):
    if (i, j) in found:
        return

    found.add((i, j))

    for x, y in neighbours(i, j, matrix):
        curr = matrix[x][y]
        if curr >= matrix[i][j] and curr != 9:
            dfs(x, y, found, matrix)


def part1(matrix):
    ans = 0
    for i, j in lows(matrix):
        ans += matrix[i][j] + 1

    return ans


def part2(matrix):
    last = 0
    found = set()
    sizes = []

    for i, j in lows(matrix):
        dfs(i, j, found, matrix)
        sizes.append(len(found) - last)
        last = len(found)

    return prod(sorted(sizes)[-3:])
