with open("input.txt") as inputs:
    lines = inputs.read().splitlines()

    points = []
    for line in lines:
        if line == "":
            break
        x, y = line.split(",")
        points.append((int(x), int(y)))

    folds = []
    for line in reversed(lines):
        if line == "":
            break
        axis, num = line.split("=")
        folds.append((axis[-1], int(num)))
    folds.reverse()


def fold(axis, num, x, y):
    if axis == "y" and y > num:
        y = 2 * num - y
    if axis == "x" and x > num:
        x = 2 * num - x
    return x, y


def pprint(points):
    xs = [x for x, y in points]
    ys = [y for x, y in points]

    for j in range(min(ys), max(ys) + 1):
        s = ""
        for i in range(min(xs), max(xs) + 1):
            s += "#" if (i, j) in points else "."
        print(s)


def part1(points, folds):
    axis, num = folds[0]
    out = set()
    for x, y in points:
        new = fold(axis, num, x, y)
        out.add(new)

    return len(out)


def part2(points, folds):
    for axis, num in folds:
        after = set()
        for x, y in points:
            new = fold(axis, num, x, y)
            after.add(new)
        points = after

    pprint(points)
