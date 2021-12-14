from collections import Counter
from math import ceil

with open("input.txt") as inputs:
    lines = inputs.read().splitlines()

    template = lines[0]
    polymer = Counter((a, b) for a, b in zip(template, template[1:]))

    rules = {}
    for line in lines[2:]:
        pair, result = line.split(" -> ")
        a, b = pair
        rules[(a, b)] = result


def step(polymer, rules):
    after = Counter()

    for pair in polymer:
        first = pair[0], rules[pair]
        second = rules[pair], pair[1]

        after[first] += polymer[pair]
        after[second] += polymer[pair]

    return after


def score(polymer):
    counts = Counter()

    for (first, second), n in polymer.items():
        counts[first] += n
        counts[second] += n

    most = counts.most_common()[0][1]
    least = counts.most_common()[-1][1]

    return ceil(most / 2) - ceil(least / 2)


def part1(polymer, rules):
    for _ in range(10):
        polymer = step(polymer, rules)

    return score(polymer)


def part2(polymer, rules):
    for _ in range(40):
        polymer = step(polymer, rules)

    return score(polymer)
