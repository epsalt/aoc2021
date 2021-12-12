from collections import defaultdict

with open("input.txt") as inputs:
    lines = inputs.read().splitlines()
    edges = defaultdict(list)
    for line in lines:
        start, end = line.split("-")
        edges[start].append(end)
        edges[end].append(start)


def find_routes(edges, double=None):
    paths = set()

    def route(curr, edges, path=()):
        options = edges[curr]
        if curr == "end":
            paths.add(path)

        curr = (curr,)
        path = path + curr

        for option in options:
            if (
                option.isupper()
                or option not in path
                or (option == double and path.count(option) < 2)
            ):
                route(option, edges, path)

    route("start", edges)
    return paths


def part1(edges):
    return len(find_routes(edges))


def part2(edges):
    all_paths = set()

    for vert in edges:
        if vert.islower() and vert not in ("start", "end"):
            all_paths.update(find_routes(edges, vert))

    return len(all_paths)
