from itertools import count

with open("input.txt") as inputs:
    state = {}
    for i, line in enumerate(inputs.read().splitlines()):
        for j, char in enumerate(line):
            state[(i, j)] = char
        r, c = max(i for i, j in state), max(j for i, j in state)


def step(state, r, c):
    after = {}

    for (i, j), curr in state.items():
        if curr == ">":
            if j < c and state[(i, j + 1)] == ".":
                after[(i, j)] = "."
                after[(i, j + 1)] = ">"
            elif j == c and state[(i, 0)] == ".":
                after[(i, j)] = "."
                after[(i, 0)] = ">"
            else:
                after[(i, j)] = ">"
        elif (i, j) not in after:
            after[(i, j)] = curr

    state = after
    after = {}

    for (i, j), curr in state.items():
        if curr == "v":
            if i < r and state[(i + 1, j)] == ".":
                after[(i, j)] = "."
                after[(i + 1, j)] = "v"
            elif i == r and state[(0, j)] == ".":
                after[(i, j)] = "."
                after[(0, j)] = "v"
            else:
                after[(i, j)] = "v"
        elif (i, j) not in after:
            after[(i, j)] = curr

    return after


def part1(state, r, c):
    for i in count(1):
        last = state
        state = step(state, r, c)

        if state == last:
            return i
