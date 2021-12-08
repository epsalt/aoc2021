from itertools import permutations

with open("input.txt") as inputs:
    lines = []
    for row in inputs:
        row = row.strip()
        first, second = row.split(" | ")
        lines.append([first.split(" "), second.split(" ")])


codes = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]


def get_mapping(words, codeset):
    for permutation in permutations("abcdefg"):
        mapping = {p: l for l, p in zip("abcdefg", permutation)}

        new_words = set()
        for word in words:
            new_words.add("".join(sorted(mapping[letter] for letter in word)))
            if codeset == new_words:
                return mapping


def part1(lines):
    ans = 0

    for first, second in lines:
        for word in second:
            if len(word) in (2, 3, 4, 7):
                ans += 1

    return ans


def part2(lines, codes):
    ans = 0
    codeset = set(codes)
    for line in lines:
        first, second = line
        mapping = get_mapping(first + second, codeset)

        num = 0
        for i, word in enumerate(reversed(second)):
            decoded = "".join(sorted(mapping[letter] for letter in word))
            num += 10 ** i * codes.index(decoded)

        ans += int(num)

    return ans
