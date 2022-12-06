def calPoints(boards: list[list[int, bool]], bingoNum: int) -> int:
    ans = 0
    for row in boards:
        temp = [ele[0] for ele in row if ele[1] == False]
        ans += sum(temp)

    return ans * bingoNum


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

    totalBoards.append(boards)  # add last board

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
