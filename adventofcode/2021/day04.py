# test case
testBingoNums = [
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

# actual input
bingoNums = [
    28,
    82,
    77,
    88,
    95,
    55,
    62,
    21,
    99,
    14,
    30,
    9,
    97,
    92,
    94,
    3,
    60,
    22,
    18,
    86,
    78,
    71,
    61,
    43,
    79,
    33,
    65,
    81,
    26,
    49,
    47,
    51,
    0,
    89,
    57,
    75,
    42,
    35,
    80,
    1,
    46,
    83,
    39,
    53,
    40,
    36,
    54,
    70,
    76,
    38,
    50,
    23,
    67,
    2,
    20,
    87,
    37,
    66,
    84,
    24,
    98,
    4,
    7,
    12,
    44,
    10,
    29,
    5,
    48,
    59,
    32,
    41,
    90,
    17,
    56,
    85,
    96,
    93,
    27,
    74,
    45,
    25,
    15,
    6,
    69,
    16,
    19,
    8,
    31,
    13,
    64,
    63,
    34,
    73,
    58,
    91,
    11,
    68,
    72,
    52,
]


class BingoNum:
    def __init__(self, num: int):
        self.num = num
        self.isNumBingo = False


class Board:
    def __init__(self, rows: list[list[BingoNum]]):
        self.rows = rows
        self.cols = self.transpose(rows)
        self.isBoardBingo = False

    def transpose(self, rows: list[list[BingoNum]]) -> list[list[BingoNum]]:
        cols = []
        for i in range(len(rows[0])):
            cols.append([row[i] for row in rows])
        return cols

    def isBingo(self) -> bool:
        for row in self.rows:
            if all(ele.isNumBingo for ele in row):
                return True
        for col in self.cols:
            if all(ele.isNumBingo for ele in col):
                return True
        return False

    def calPoints(self, bingoNum: int) -> int:
        ans = 0
        for row in self.rows:
            temp = [ele.num for ele in row if ele.isNumBingo == False]
            ans += sum(temp)
        return ans * bingoNum


def createBoards(data: list[str]) -> list[Board]:
    rows: list[list[BingoNum]] = []
    allBoards: list[Board] = []

    for line in data:
        if line == "" or line == "end":
            allBoards.append(Board(rows))
            rows = []
        else:
            temp = list(map(int, line.split()))
            temp = [BingoNum(ele) for ele in temp]
            rows.append(temp)

    return allBoards


def part1(data: list[str], bingoNums: list[int]) -> int:
    ans = 0
    allBoards = createBoards(data)

    for num in bingoNums:
        for board in allBoards:
            for row in board.rows:
                for ele in row:
                    if ele.num == num:
                        ele.isNumBingo = True
            for col in board.cols:
                for ele in col:
                    if ele.num == num:
                        ele.isNumBingo = True

        for board in allBoards:
            board.isBoardBingo = board.isBingo()

            if board.isBoardBingo:
                ans = board.calPoints(num)
                break

        if ans != 0:
            break

    print(ans)
    return ans


def part2(data: list[str], bingoNums: list[int]) -> int:
    ans = 0
    allBoards = createBoards(data)

    for num in bingoNums:
        for board in allBoards:
            for row in board.rows:
                for ele in row:
                    if ele.num == num:
                        ele.isNumBingo = True
            for col in board.cols:
                for ele in col:
                    if ele.num == num:
                        ele.isNumBingo = True

        for board in allBoards:
            board.isBoardBingo = board.isBingo()

        if len(allBoards) > 1:
            allBoards = [board for board in allBoards if board.isBoardBingo == False]
        else:
            if allBoards[0].isBoardBingo:
                ans = allBoards[0].calPoints(num)
                break

    print(ans)
    return ans


def test_passing():
    with open("test.txt", "r") as f:
        data = f.read().splitlines()
        assert part1(data, testBingoNums) == 4512
        assert part2(data, testBingoNums) == 1924
        f.close()


with open("day04.txt", "r") as f:
    data = f.read().splitlines()

    # part1(data, bingoNums)

    part2(data, bingoNums)

    test_passing()

    f.close()
