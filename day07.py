with open("input.txt") as inputs:
    nums = [int(i) for i in inputs.read().split(",")]


def linear(nums, position):
    fuel = 0
    for num in nums:
        fuel += abs(num - position)

    return fuel


def triangular(nums, position):
    fuel = 0
    for num in nums:
        dist = abs(num - position)
        fuel += dist * (dist + 1) // 2

    return fuel


def part1(nums):
    return min(linear(nums, fuel) for fuel in nums)


def part2(nums):
    return min(triangular(nums, fuel) for fuel in nums)
