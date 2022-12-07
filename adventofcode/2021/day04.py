bingoNums = [
    7,
    4,
    9,
    5,
    11,
    17,
    23,
    2,
    0,
    14,
    21,
    24,
    10,
    16,
    13,
    6,
    15,
    25,
    12,
    22,
    18,
    20,
    8,
    19,
    3,
    26,
    1,
]

# bingoNums = [28,82,77,88,95,55,62,21,99,14,30,9,97,92,94,3,60,22,18,86,78,71,61,43,79,33,65,81,26,49,47,51,0,89,57,75,42,35,80,1,46,83,39,53,40,36,54,70,76,38,50,23,67,2,20,87,37,66,84,24,98,4,7,12,44,10,29,5,48,59,32,41,90,17,56,85,96,93,27,74,45,25,15,6,69,16,19,8,31,13,64,63,34,73,58,91,11,68,72,52]
def calPoints(boards: list[list[int, bool]], bingoNum: int) -> int:
    ans = 0
    for row in boards:
        temp = [ele[0] for ele in row if ele[1] == False]
        ans += sum(temp)

    return ans * bingoNum


def createBoards(data: list[str]) -> list[list[list[int, bool]]]:
    currentBoard = []
    allBoards = []

    for line in data:
        if line == "":
            allBoards.append(currentBoard)
            currentBoard = []
        else:
            temp = list(map(int, line.split()))
            temp = [[ele, False] for ele in temp]
            currentBoard.append(temp)


def part1(data: list[str]):
    ans = 0
    bingoNums = list(map(int, data[0].split(",")))
    boards = []
    totalBoards = []

    i = 2
    while i < len(data):
        if data[i] == "":
            totalBoards.append(boards)
            boards = []
        else:
            temp = list(map(int, data[i].split()))
            temp = [[ele, False] for ele in temp]
            boards.append(temp)

        i += 1

    for bingoNum in bingoNums:
        for boards in totalBoards:
            for board in boards:
                for ele in board:
                    if ele[0] == bingoNum:
                        ele[1] = True

        for boards in totalBoards:
            for board in boards:
                if all([ele[1] for ele in board]):
                    ans = calPoints(boards, bingoNum)
                    break

            i = 0
            while i < len(boards):
                if all(
                    [
                        boards[0][i][1],
                        boards[1][i][1],
                        boards[2][i][1],
                        boards[3][i][1],
                        boards[4][i][1],
                    ]
                ):
                    ans = calPoints(boards, bingoNum)
                    break
                else:
                    i += 1

        if ans != 0:
            break

    print(ans)


def part2(data: list[str]):
    ans = 0

    print(ans)


with open("test.txt", "r") as f:
    # with open("day04.txt", "r") as f:
    data = f.read().splitlines()

    part1(data)

    # part2(data)

    f.close()
