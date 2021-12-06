from collections import Counter

with open("input.txt") as inputs:
    nums = [int(i) for i in inputs.read().split(",")]


def simulate(nums, n):
    today = Counter(nums)

    for _ in range(n):
        tomorrow = Counter()

        for k, value in today.items():
            if k == 0:
                tomorrow[8] += value
                tomorrow[6] += value
            else:
                tomorrow[k - 1] += value

        today = tomorrow

    return sum(today.values())


def part1(nums):
    return simulate(nums, 80)


def part2(nums):
    return simulate(nums, 256)
