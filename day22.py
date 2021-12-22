import re
from math import prod

with open("input.txt") as inputs:
    steps = []
    for i, line in enumerate(inputs.read().splitlines()):
        state, ranges = line.split(" ")
        dims = [int(c) for c in re.findall(r"-?\d+", ranges)]
        dims = (dims[0], dims[1]), (dims[2], dims[3]), (dims[4], dims[5])

        steps.append((state, dims))


def line_int(a, b):
    if (b[0] > a[1]) or (a[0] > b[1]):
        return None

    return max(a[0], b[0]), min(a[1], b[1])


def cube_difference(a, b):
    cubes = []
    xint = line_int(a[0], b[0])
    yint = line_int(a[1], b[1])
    zint = line_int(a[2], b[2])

    # xint, all y, all z
    cubes.append(((a[0][0], xint[0] - 1), a[1], a[2]))
    cubes.append(((xint[1] + 1, a[0][1]), a[1], a[2]))

    # xint, yint, all z
    cubes.append((xint, (a[1][0], yint[0] - 1), a[2]))
    cubes.append((xint, (yint[1] + 1, a[1][1]), a[2]))

    # zint, yint, zint
    cubes.append((xint, yint, (a[2][0], zint[0] - 1)))
    cubes.append((xint, yint, (zint[1] + 1, a[2][1])))

    return [cube for cube in cubes if (all(cube[n][0] <= cube[n][1] for n in range(3)))]


def cube_intersection(a, b):
    cube = []
    for n in range(0, 3):
        intersection = line_int(a[n], b[n])
        if intersection is None:
            return None
        cube.append((intersection[0], intersection[1]))

    return cube


def combine(steps):
    cubes = []
    for state, curr in steps:
        after = [curr] if state == "on" else []
        for cube in cubes:
            if not cube_intersection(cube, curr):
                after.append(cube)
            else:
                for diff in cube_difference(cube, curr):
                    after.append(diff)

        cubes = after

    return cubes


def count(cubes):
    score = 0
    for cube in cubes:
        score += prod(cube[n][1] - cube[n][0] + 1 for n in range(3))
    return score


def part1(steps):
    cubes = combine(steps)
    bounds = ((-50, 50), (-50, 50), (-50, 50))
    clipped = []

    for cube in cubes:
        if (intersection := cube_intersection(cube, bounds)) is not None:
            clipped.append(intersection)

    return count(clipped)


def part2(steps):
    cubes = combine(steps)
    return count(cubes)
