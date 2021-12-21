from itertools import cycle, islice, product
from collections import Counter


def turn(rolls, position, score):
    inc = sum(rolls)
    position = (position + inc - 1) % 10 + 1
    score += position

    return position, score


def part1(pos1, pos2):
    score1 = score2 = 0
    dice = cycle(range(1, 101))
    rolls = 0

    while True:
        pos1, score1 = turn(islice(dice, 3), pos1, score1)
        rolls += 3
        if score1 >= 1000:
            return rolls * score2

        pos2, score2 = turn(islice(dice, 3), pos2, score2)
        rolls += 3
        if score2 >= 1000:
            return rolls * score1


def part2(pos1, pos2, threshold=21):
    curr = Counter([((pos1, 0), (pos2, 0))])
    wins = [0, 0]

    while curr:
        after = Counter()
        for ((pos1, score1), (pos2, score2)), count in curr.items():
            for roll in product(range(1, 4), repeat=6):
                new_pos1, new_score1 = turn(roll[0:3], pos1, score1)
                if new_score1 >= threshold:
                    wins[0] += count
                    continue

                new_pos2, new_score2 = turn(roll[3:], pos2, score2)
                if new_score2 >= threshold:
                    wins[1] += count
                    continue

                state = ((new_pos1, new_score1), (new_pos2, new_score2))
                after[state] += count

        curr = after

    return max(wins) // 27
