import re

with open("input.txt") as inputs:
    data = inputs.read().strip()
    dims = [int(c) for c in re.findall(r"-?\d+", data)]


def simulate(vx, vy, dims):
    xstart, xend, ystart, yend = dims
    x = y = apex = 0

    while y > ystart and x < xend:
        apex = max(apex, y)
        x, y = x + vx, y + vy
        vx, vy = max(0, vx - 1), vy - 1

        if xstart <= x <= xend and ystart <= y <= yend:
            return apex

    return None


def solve(dims):
    xstart, xend, ystart, yend = dims
    apexes = []

    for vx in range(0, xend + 1):
        for vy in range(ystart, -ystart + 1):
            if (apex := simulate(vx, vy, dims)) is not None:
                apexes.append(apex)

    return apexes


def part1(dims):
    return max(solve(dims))


def part2(dims):
    return len(solve(dims))
