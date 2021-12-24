with open("input.txt") as inputs:
    instructions = []
    for line in inputs.read().splitlines():
        op, *variables = line.split(" ")
        instructions.append((op, variables))


def decompiled_program(w, z, ins):
    """
    i = 1 when j > 0
    i = 26 when j < 0

    When x != 0 add (w + k) in base 26 to z
    When x == 0 pop base 26 digit off of z
    """

    i = int(ins[4][1][1])
    j = int(ins[5][1][1])
    k = int(ins[15][1][1])

    x = (z % 26) + j != w
    z = (z // i) * (25 * x + 1) + (w + k) * x

    return z


def get_diffs(instructions):
    groups = []

    for n in range(0, len(instructions), 18):
        group = instructions[n : n + 18]
        i = int(group[4][1][1])
        j = int(group[5][1][1])
        k = int(group[15][1][1])
        groups.append((i, j, k))

    stack = []
    for n, (i, j, k) in enumerate(groups):
        if i == 1:
            stack.append((n, (i, j, k)))
        else:
            m, (i2, j2, k2) = stack.pop()
            yield m, n, k2 + j


def part1(instructions):
    ans = [0] * 14
    for m, n, diff in get_diffs(instructions):
        if diff > 0:
            ans[m] = 9 - diff
            ans[n] = 9

        else:
            ans[n] = 9 + diff
            ans[m] = 9

    return int("".join(map(str, ans)))


def part2(instructions):
    ans = [0] * 14
    for m, n, diff in get_diffs(instructions):
        if diff > 0:
            ans[m] = 1
            ans[n] = 1 + diff

        else:
            ans[n] = 1
            ans[m] = 1 - diff

    return int("".join(map(str, ans)))
