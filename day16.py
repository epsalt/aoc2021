from math import prod

with open("input.txt") as inputs:
    hex_string = inputs.read().strip()


def parse(hex_string):
    lookup = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }

    binary = "".join(lookup[char] for char in hex_string)
    return binary


def get_packet_id(bits):
    start, end = 0, 3
    version = int(bits[start:end], 2)

    start, end = 3, 6
    id = int(bits[start:end], 2)

    return version, id, bits[end:]


def literal(bits):
    groups = []
    i = 0
    while bits[i] != "0":
        groups.append(bits[i + 1 : i + 5])
        i += 5

    groups.append(bits[i + 1 : i + 5])
    return bits[i + 5 :], int("".join(groups), 2)


def read_packet(bits):
    version, id, bits = get_packet_id(bits)

    if id == 4:
        bits, payload = literal(bits)
        return [bits, version, id, payload]

    elif bits[0] == "0":
        bits = bits[1:]
        length = int(bits[:15], 2)
        start = curr = bits[15:]

        payloads = []
        while len(start) - len(curr) < length:
            payload = read_packet(curr)
            payloads.append(payload)
            curr = payload[0]

        return [curr, version, id, payloads]

    elif bits[0] == "1":
        bits = bits[1:]
        count = int(bits[:11], 2)
        curr = bits[11:]

        payloads = []
        for _ in range(count):
            payload = read_packet(curr)
            payloads.append(payload)
            curr = payload[0]

        return [curr, version, id, payloads]


def evaluate(instruction, ops):
    bits, version, id, payload = instruction

    if id == 4:
        return payload

    children = [evaluate(child, ops) for child in payload]
    return ops[id](children)


def part1(hex_string):
    bits = parse(hex_string)
    instructions = [read_packet(bits)]
    versions = 0

    while instructions:
        bits, version, id, payload = instructions.pop()
        versions += version

        if isinstance(payload, list):
            instructions.extend(payload)

    return versions


def part2(hex_string):
    ops = {
        0: lambda x: sum(x),
        1: lambda x: prod(x),
        2: lambda x: min(x),
        3: lambda x: max(x),
        5: lambda x: int(x[0] > x[1]),
        6: lambda x: int(x[0] < x[1]),
        7: lambda x: int(x[0] == x[1]),
    }

    bits = parse(hex_string)
    instruction = read_packet(bits)

    return evaluate(instruction, ops)
