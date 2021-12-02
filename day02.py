with open("input.txt") as inputs:
    entries = []
    for entry in inputs:
        direction, num = entry.split()
        entries.append((direction, int(num)))


def part1(entries):
    hz = vert = 0

    for direction, num in entries:
        if direction == "up":
            vert -= num
        elif direction == "down":
            vert += num
        elif direction == "forward":
            hz += num

    return hz * vert


def part2(entries):
    aim = hz = vert = 0

    for direction, num in entries:
        if direction == "up":
            aim -= num
        elif direction == "down":
            aim += num
        elif direction == "forward":
            hz += num
            vert += aim * num

    return hz * vert
