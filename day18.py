from math import ceil, floor
from itertools import permutations
from copy import deepcopy


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(pair):
    if isinstance(pair, int):
        return Node(val=pair)

    left, right = pair
    return Node(left=build_tree(left), right=build_tree(right))


with open("input.txt") as inputs:
    nodes = []
    for line in inputs:
        nodes.append(build_tree(eval(line.strip())))


def split(node):
    found = False

    def dfs(node):
        nonlocal found

        if node.val is not None and not found and node.val >= 10:
            node.left = Node(val=floor(node.val / 2))
            node.right = Node(val=ceil(node.val / 2))
            node.val = None
            found = True
            return

        if node.val is not None:
            return

        dfs(node.left)
        dfs(node.right)

    dfs(node)
    return found


def explode(node):
    found = False
    last = None
    carry = None

    def dfs(node, n=0):
        nonlocal found, last, carry

        if n == 4 and node.val is None and found is False:
            carry = node.right.val

            if last is not None:
                last.val += node.left.val

            found = True
            node.val = 0
            node.left = node.right = None
            return

        if node.val is not None:
            last = node
            if carry is not None:
                node.val += carry
                carry = None
            return

        dfs(node.left, n + 1)
        dfs(node.right, n + 1)

    dfs(node, 0)
    return found


def addreduce(a, b):
    node = Node(left=deepcopy(a), right=deepcopy(b))
    while True:
        if not explode(node):
            if not split(node):
                return node


def magnitude(node):
    if node.val is not None:
        return node.val

    return 3 * magnitude(node.left) + 2 * magnitude(node.right)


def part1(nodes):
    curr = None
    for node in nodes:
        curr = addreduce(curr, node) if curr is not None else node

    return magnitude(curr)


def part2(nodes):
    highest = 0

    for a, b in permutations(nodes, 2):
        highest = max(highest, magnitude(addreduce(a, b)))

    return highest
