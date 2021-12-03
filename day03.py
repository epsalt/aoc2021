with open("input.txt") as inputs:
    nums = [int(i, 2) for i in inputs]
    length = max(num.bit_length() for num in nums)


def part1(nums, length):
    counts = [0] * length

    for num in nums:
        for i in range(length):
            counts[i] += num & 1
            num = num >> 1

    gamma = epsilon = 0
    for i, count in enumerate(counts):
        if count > (len(nums) // 2):
            gamma |= 1 << i
        else:
            epsilon |= 1 << i

    return gamma * epsilon


def part2(nums, length):
    return helper(nums, length, 0) * helper(nums, length, 1)


def helper(nums, length, goal):
    for i in range(length - 1, -1, -1):
        count = sum((num >> i) & 1 for num in nums)

        if count >= (len(nums) - count):
            winner = goal
        else:
            winner = int(not goal)

        nums = [num for num in nums if ((num >> i) & 1) == winner]

        if len(nums) == 1:
            return nums[0]
