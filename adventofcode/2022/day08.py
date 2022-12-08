def createMaps(data: list[str]) -> list[list[int]]:
    maps = []
    for line in data:
        temp = [int(ele) for ele in line]
        maps.append(temp)
    return maps


def checkLeftIsVisible(maps: list[list[int]], i: int, j: int, target: int):
    for k in range(j - 1, -1, -1):
        if maps[i][k] >= target:
            return 0
    return 1


def checkRightIsVisible(maps: list[list[int]], i: int, j: int, target: int):
    for k in range(j + 1, len(maps[i])):
        if maps[i][k] >= target:
            return 0
    return 1


def checkUpIsVisible(maps: list[list[int]], i: int, j: int, target: int):
    for k in range(i - 1, -1, -1):
        if maps[k][j] >= target:
            return 0
    return 1


def checkDownIsVisible(maps: list[list[int]], i: int, j: int, target: int):
    for k in range(i + 1, len(maps)):
        if maps[k][j] >= target:
            return 0
    return 1


def part1(data: list[str]):
    maps = createMaps(data)

    visibles = 0

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if i == 0 or i == len(maps) - 1 or j == 0 or j == len(maps[i]) - 1:
                visibles += 1
                continue

            isVisible = 0
            isVisible += checkLeftIsVisible(maps, i, j, maps[i][j])
            isVisible += checkRightIsVisible(maps, i, j, maps[i][j])
            isVisible += checkUpIsVisible(maps, i, j, maps[i][j])
            isVisible += checkDownIsVisible(maps, i, j, maps[i][j])
            if isVisible > 0:
                visibles += 1

    print(visibles)


def checkLeftNum(maps: list[list[int]], i: int, j: int, target: int):
    count = 0
    for k in range(j - 1, -1, -1):
        if maps[i][k] >= target:
            count += 1
            return count
        else:
            count += 1
    return count


def checkRightNum(maps: list[list[int]], i: int, j: int, target: int):
    count = 0
    for k in range(j + 1, len(maps[i])):
        if maps[i][k] >= target:
            count += 1
            return count
        else:
            count += 1
    return count


def checkUpNum(maps: list[list[int]], i: int, j: int, target: int):
    count = 0
    for k in range(i - 1, -1, -1):
        if maps[k][j] >= target:
            count += 1
            return count
        else:
            count += 1
    return count


def checkDownNum(maps: list[list[int]], i: int, j: int, target: int):
    count = 0
    for k in range(i + 1, len(maps)):
        if maps[k][j] >= target:
            count += 1
            return count
        else:
            count += 1
    return count


def part2(data: list[str]):
    maps = createMaps(data)

    maxscore = 1

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if i == 0 or i == len(maps) - 1 or j == 0 or j == len(maps[i]) - 1:
                continue

            currentscore = 1
            currentscore *= checkLeftNum(maps, i, j, maps[i][j])
            currentscore *= checkRightNum(maps, i, j, maps[i][j])
            currentscore *= checkUpNum(maps, i, j, maps[i][j])
            currentscore *= checkDownNum(maps, i, j, maps[i][j])

            maxscore = max(maxscore, currentscore)

    print(maxscore)


# with open("test.txt", "r") as f:
with open("day08.txt", "r") as f:
    data = f.read().splitlines()

    # part1(data)

    part2(data)

    f.close()
