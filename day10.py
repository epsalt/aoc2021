with open("input.txt") as inputs:
    lines = inputs.read().splitlines()


matches = {"(": ")", "[": "]", "{": "}", "<": ">"}


def part1(lines, matches):
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    ans = 0
    for line in lines:
        stack = []

        for char in line:
            if char in matches:
                stack.append(char)
            else:
                opening = stack.pop()
                if matches[opening] != char:
                    ans += points[char]
                    break

    return ans


def part2(lines, matches):
    points = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []

    for line in lines:
        score = 0
        corrupted = False
        stack = []

        for char in line:
            if char in matches:
                stack.append(char)
            else:
                opening = stack.pop()
                if matches[opening] != char:
                    corrupted = True
                    break

        if not corrupted:
            for opening in reversed(stack):
                closing = matches[opening]
                score = score * 5 + points[closing]
            scores.append(score)

    return sorted(scores)[len(scores) // 2]
