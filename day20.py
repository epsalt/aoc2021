with open("input.txt") as inputs:
    image = {}
    for i, line in enumerate(inputs.read().splitlines()):
        if i == 0:
            algo = line
        elif line:
            for j, char in enumerate(line):
                image[(i - 2, j)] = char


def square(i, j, image, oob):
    for x in (i - 1, i, i + 1):
        for y in (j - 1, j, j + 1):
            if (x, y) in image:
                yield image[(x, y)]
            else:
                yield oob


def square_num(square):
    bits = ""
    for char in square:
        bits += "0" if char == "." else "1"

    return int(bits, 2)


def step(algo, image, oob):
    new_image = {}
    xs = [x for x, y in image.keys()]
    ys = [y for x, y in image.keys()]
    xs, ys = (min(xs), max(xs)), (min(ys), max(ys))

    for x in range(xs[0] - 3, xs[1] + 4):
        for y in range(ys[0] - 3, ys[1] + 4):
            num = square_num(square(x, y, image, oob))
            char = algo[num]
            new_image[(x, y)] = char

    return new_image


def count_pixels(algo, image, steps):
    oob = "."
    for _ in range(steps):
        image = step(algo, image, oob)
        oob = "#" if oob == "." else "."

    return sum(1 for char in image.values() if char == "#")


def part1(algo, image):
    return count_pixels(algo, image, 2)


def part2(algo, image):
    return count_pixels(algo, image, 50)
