from collections import namedtuple, Counter


Point = namedtuple("Point", ["x", "y"])
Line = namedtuple("Line", ["start", "end"])

with open("input.txt") as inputs:
    lines = []
    for row in inputs:
        start, end = row.split(" -> ")
        start = Point(*(int(num) for num in start.split(",")))
        end = Point(*(int(num) for num in end.split(",")))
        lines.append(Line(start, end))


def hz_vert_only(lines):
    for line in lines:
        slope, b = eq(line)
        if slope == 0 or slope == float("inf"):
            yield line


def eq(line):
    start, end = line
    xdiff = end.x - start.x

    if xdiff == 0:
        return float("inf"), start.x

    slope = (end.y - start.y) / (end.x - start.x)
    b = start.y - slope * start.x

    return slope, b


def simulate(lines):
    grid = Counter()

    for line in lines:
        slope, b = eq(line)

        if slope == float("inf"):
            start = min(line.start.y, line.end.y)
            end = max(line.start.y, line.end.y)

            for y in range(start, end + 1):
                grid[(line.start.x, y)] += 1

        else:
            start = min(line.start.x, line.end.x)
            end = max(line.start.x, line.end.x)

            for x in range(start, end + 1):
                y = slope * x + b
                grid[(x, int(y))] += 1

    return sum(1 for val in grid.values() if val > 1)


def part1(lines):
    lines = hz_vert_only(lines)
    return simulate(lines)


def part2(lines):
    return simulate(lines)
