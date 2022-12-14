from __future__ import annotations
from collections import defaultdict


def getValue(input: str) -> int:
    if input != "S" and input != "E":
        return ord(input)
    elif input == "S":
        return ord("a")
    else:
        return ord("z")


def createGraph(data: list[str]) -> dict[str, list[str]]:
    graph = defaultdict(list)
    w = len(data[0])
    h = len(data)

    for i in range(h):
        for j in range(w):
            currentValue = getValue(data[i][j])

            if i > 0:
                neighbourValue = getValue(data[i - 1][j])
                if currentValue + 1 >= neighbourValue:
                    graph[(i, j)].append((i - 1, j))

            if i < h - 1:
                neighbourValue = getValue(data[i + 1][j])
                if currentValue + 1 >= neighbourValue:
                    graph[(i, j)].append((i + 1, j))

            if j > 0:
                neighbourValue = getValue(data[i][j - 1])
                if currentValue + 1 >= neighbourValue:
                    graph[(i, j)].append((i, j - 1))

            if j < w - 1:
                neighbourValue = getValue(data[i][j + 1])
                if currentValue + 1 >= neighbourValue:
                    graph[(i, j)].append((i, j + 1))

    return graph


def BFS_SP(graph, start, goal) -> int:
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return 9999

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    # print("Shortest path = ", *new_path)
                    print("Length of shortest path = ", len(new_path) - 1)
                    return len(new_path) - 1
            explored.append(node)

    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting" "path doesn't exist :(")
    return 9999


def findChar(data: list[str], char: str) -> tuple[int, int]:
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == char:
                return (i, j)

    return (-1, -1)


def findStartOption(data: list[str]) -> list[tuple[int, int]]:
    startOption = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "a" or data[i][j] == "S":
                startOption.append((i, j))

    return startOption


def part1(data: list[str]) -> int:
    graph = createGraph(data)
    start = findChar(data, "S")
    end = findChar(data, "E")

    ans = BFS_SP(graph, start, end)

    return ans


def part2(data: list[str]) -> int:
    graph = createGraph(data)
    end = findChar(data, "E")
    startOption = findStartOption(data)

    ans = 9999
    for start in startOption:
        ans = min(ans, BFS_SP(graph, start, end))

    print("Part2 Ans = ", ans)
    return ans


def test_passing():
    with open("test.txt", "r") as f:
        data = f.read().splitlines()
        # assert part1(data) == 31
        assert part2(data) == 29
        f.close()


with open("day12.txt", "r") as f:
    data = f.read().splitlines()

    # part1(data)

    part2(data)

    # test_passing()

    f.close()
