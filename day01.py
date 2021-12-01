with open("input.txt") as inputs:
    numbers = [int(i) for i in inputs]


def part1(numbers):
    ans = 0
    last = None

    for n in numbers:
        if last and n > last:
            ans += 1
        last = n

    return ans


def part2(numbers, window):
    ans = 0
    last = None

    for i in range(len(numbers) - window + 1):
        n = sum(numbers[i : i + window])
        if last and n > last:
            ans += 1
        last = n

    return ans
