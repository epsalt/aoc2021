from itertools import combinations


with open("input.txt") as inputs:
    scanners = []
    points = []
    for i, line in enumerate(inputs):
        line = line.strip()

        if line == "" or i == 0:
            pass
        elif line[:3] == "---":
            scanners.append(points)
            points = []
        else:
            x, y, z = line.split(",")
            points.append((int(x), int(y), int(z)))
    scanners.append(points)


def rotate_x(x, y, z):
    return x, z, -y


def rotate_y(x, y, z):
    return -y, x, z


def rotations(x, y, z):
    """https://stackoverflow.com/a/16467849/4501508"""
    for cycle in range(2):
        for step in range(3):
            x, y, z = rotate_x(x, y, z)
            yield (x, y, z)
            for i in range(3):
                x, y, z = rotate_y(x, y, z)
                yield (x, y, z)
        x, y, z = rotate_x(x, y, z)
        x, y, z = rotate_y(x, y, z)
        x, y, z = rotate_x(x, y, z)


def scanner_rotations(scanner):
    rots = []
    for x, y, z in scanner:
        rots.append(list(rotations(x, y, z)))

    return list(zip(*rots))


def beacon_offsets(scanner):
    offsets = []
    for a in scanner:
        offset = set()
        for b in scanner:
            if a != b:
                offset.add((b[0] - a[0], b[1] - a[1], b[2] - a[2]))
        offsets.append(offset)

    return offsets


def compare(a, b, threshold):
    offsets_a = beacon_offsets(a)

    for i, beacon_a in enumerate(offsets_a):
        for rot_b in scanner_rotations(b):
            for j, beacon_b in enumerate(beacon_offsets(rot_b)):
                common = beacon_a.intersection(beacon_b)
                if len(common) >= threshold - 1:
                    x1, y1, z1 = a[i]
                    x2, y2, z2 = rot_b[j]
                    dx, dy, dz = x1 - x2, y1 - y2, z1 - z2
                    normalized = [(q + dx, w + dy, r + dz) for (q, w, r) in rot_b]

                    return normalized, (dx, dy, dz)


def beacon_list(scanners, threshold=12):
    todo = scanners[:]
    curr = todo.pop(0)
    q = [curr]

    beacons = set(curr)
    scanners = set([(0, 0, 0)])

    while q:
        curr = q.pop()
        found = set()

        for i, other in enumerate(todo):
            if (found_beacon := compare(curr, other, threshold)) is not None:
                beacon, offset = found_beacon
                beacons.update(beacon)
                scanners.add(offset)

                q.append(beacon)
                found.add(i)

        todo = [b for i, b in enumerate(todo) if i not in found]

    return beacons, scanners


def part1(scanners):
    beacons, scanners = beacon_list(scanners)

    return len(beacons)


def part2(scanners):
    beacons, scanners = beacon_list(scanners)
    dist = 0

    for a, b in combinations(scanners, 2):
        x, y, z = a
        i, j, k = b
        dist = max(dist, abs(x - i) + abs(y - j) + abs(z - k))

    return dist
