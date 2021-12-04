with open("input.txt") as inputs:
    boards = []
    board = None

    for i, line in enumerate(inputs.read().splitlines()):
        if i == 0:
            nums = [int(char) for char in line.split(",")]
        elif line.strip() == "":
            if board is not None:
                boards.append(board)
            board = []
        else:
            row = [int(char) for char in line.split()]
            board.append(row)

    boards.append(board)


def next_winner(nums, marked, boards):
    for num in nums:
        marked.add(num)
        for board in boards:
            for row in board:
                if all(cell in marked for cell in row):
                    return board, marked, num

            for col in zip(*board):
                if all(cell in marked for cell in col):
                    return board, marked, num


def score(board, marked, num):
    unmarked = 0

    for row in board:
        for cell in row:
            if cell not in marked:
                unmarked += cell

    return unmarked * num


def part1(nums, boards):
    marked = set()
    board, marked, num = next_winner(nums, marked, boards)

    return score(board, marked, num)


def part2(nums, boards):
    marked = set()

    while len(boards):
        winner, marked, num = next_winner(nums, marked, boards)
        boards = [board for board in boards if board != winner]
        nums = nums[nums.index(num) :]

        if len(boards) == 1:
            last = boards[0]

    return score(last, marked, num)
