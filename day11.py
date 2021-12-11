from itertools import product


with open("input.txt") as inputs:
    lines = inputs.read().splitlines()


def parse(lines):
    data = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            data[(i, j)] = int(char)

    return data


def neighbours(i, j):
    for dx, dy in product((-1, 0, 1), (-1, 0, 1)):
        if dx or dy:
            yield i + dx, j + dy


def flash(coords, flashed, data):
    flashed.add(coords)
    for adj in neighbours(*coords):
        if adj in data and adj not in flashed:
            data[adj] += 1
            if data[adj] > 9:
                flashed, data = flash(adj, flashed, data)

    return flashed, data


def step(data):
    flashed = set()
    for coords in data:
        data[coords] += 1
        if data[coords] > 9 and coords not in flashed:
            flashed, data = flash(coords, flashed, data)

    for coords in data:
        if data[coords] > 9:
            data[coords] = 0

    return data, flashed


def part1(lines):
    data = parse(lines)
    ans = 0

    for _ in range(100):
        data, flashed = step(data)
        ans += len(flashed)

    return ans


def part2(lines):
    data = parse(lines)
    ans = 0

    while not ans or len(flashed) != len(data):
        data, flashed = step(data)
        ans += 1

    return ans
