from copy import deepcopy

data = {
    2: ["B", "D"],
    4: ["C", "C"],
    6: ["D", "A"],
    8: ["A", "B"],
}


def solve(stacks, min_cost):
    hallway = ["."] * 11
    goals = {
        "A": 2,
        "B": 4,
        "C": 6,
        "D": 8,
    }

    def helper(stacks, hallway, goals, room_size, total_cost=0):
        nonlocal min_cost

        if total_cost > min_cost:
            return

        if done(stacks, room_size, goals):
            min_cost = min(min_cost, total_cost)
            print(min_cost)
            return

        for move in get_moves(stacks, hallway, goals):
            sc = deepcopy(stacks)
            hc = deepcopy(hallway)

            new_stacks, new_hallway, cost = make_move(move, sc, hc, room_size)
            helper(new_stacks, new_hallway, goals, room_size, total_cost + cost)

    room_size = len(stacks[2])
    helper(stacks, hallway, goals, room_size)
    return min_cost


def done(stacks, room_size, goals):
    for stack, goal in zip(stacks.values(), goals):
        if any(pod != goal for pod in stack) or len(stack) != room_size:
            return False
    return True


def get_moves(stacks, hallway, goals):
    pieces = []
    for position, stack in stacks.items():
        if stack:
            pieces.append((stack[-1], position))

    for position, piece in enumerate(hallway):
        if piece != ".":
            pieces.append((piece, position))

    moves = []
    for piece, position in pieces:
        unblocked = unblocked_positions(position, hallway)
        goal_position = goals[piece]
        goal_clean = all(pod == piece for pod in stacks[goal_position])

        if position == goal_position and goal_clean:
            positions = []

        elif goal_position in unblocked and goal_clean:
            return [(piece, position, goal_position)]

        elif position in (2, 4, 6, 8):
            positions = [pos for pos in unblocked if pos not in (2, 4, 6, 8)]

        else:
            positions = []

        moves.extend([(piece, position, to_position) for to_position in positions])

    return moves


def make_move(move, stacks, hallways, room_size):
    costs = {"A": 1, "B": 10, "C": 100, "D": 1000}

    piece, from_pos, to_pos = move
    steps = abs(to_pos - from_pos)

    if from_pos in (2, 4, 6, 8):
        stacks[from_pos].pop()
        steps += room_size - len(stacks[from_pos])
    else:
        hallways[from_pos] = "."

    if to_pos in (2, 4, 6, 8):
        stacks[to_pos].append(piece)
        steps += room_size - len(stacks[to_pos]) + 1
    else:
        hallways[to_pos] = piece

    return stacks, hallways, steps * costs[piece]


def unblocked_positions(start, hallway):
    options = range(0, 11)

    unblocked = []
    for option in options:
        blocked = option == start
        for i in range(min(start, option), max(start, option) + 1):
            if i == start:
                continue
            elif hallway[i] != ".":
                blocked = True
        if not blocked:
            unblocked.append(option)

    return unblocked


def part1(data):
    min_cost_guess = 20000
    return solve(data, min_cost_guess)


def part2(data):
    min_cost_guess = 50000

    middle = {
        2: ["D", "D"],
        4: ["B", "C"],
        6: ["A", "B"],
        8: ["C", "A"],
    }

    bigger_stacks = {key: data[key][0:1] + middle[key] + data[key][1:] for key in data}

    return solve(bigger_stacks, min_cost_guess)
