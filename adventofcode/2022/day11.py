from __future__ import annotations


class Monkey:
    def __init__(
        self,
        items: list[int],
        operation: list[str],
        testNumber: int,
        testTrueTarget: int,
        testFalseTarget: int,
    ):
        self.items = items
        self.operation = operation
        self.testNumber = testNumber
        self.testTrueTarget = testTrueTarget
        self.testFalseTarget = testFalseTarget
        self.inspectedTimes = 0

    def receiveItem(self, item: int):
        self.items.append(item)

    def runOperation(self, item: int) -> int:
        if self.operation[1] == "old":
            value = item
        else:
            value = int(self.operation[1])

        ans = 0
        if self.operation[0] == "*":
            ans = item * value
        elif self.operation[0] == "+":
            ans = item + value

        return ans

    def reduceLevelDividedBy3(self, item: int) -> int:
        return item // 3

    def reduceLevelModByProductTestNumber(
        self, item: int, productTestNumber: int
    ) -> int:
        return item % productTestNumber

    def runTest(self, item: int, allMonkeys: list[Monkey]):
        if item % self.testNumber == 0:
            allMonkeys[self.testTrueTarget].receiveItem(item)
        else:
            allMonkeys[self.testFalseTarget].receiveItem(item)

    def inspectItemsPart1(self, allMonkeys: list[Monkey]):
        for item in self.items:
            item = self.runOperation(item)
            item = self.reduceLevelDividedBy3(item)
            self.runTest(item, allMonkeys)
            self.inspectedTimes += 1

        self.items = []

    def inspectItemsPart2(self, allMonkeys: list[Monkey], productTestNumber: int):
        for item in self.items:
            item = self.runOperation(item)
            item = self.reduceLevelModByProductTestNumber(item, productTestNumber)
            self.runTest(item, allMonkeys)
            self.inspectedTimes += 1

        self.items = []


def getItems(line: str) -> list[int]:
    _, _, *items = line.split()
    items = [int(item.replace(",", "")) for item in items]
    return items


def getOperation(line: str) -> list[str]:
    _, _, _, _, *operator = line.split()
    return operator


def getTestNumber(line: str) -> int:
    _, _, _, testNumber = line.split()
    return int(testNumber)


def getTestTarget(line: str) -> int:
    _, _, _, _, _, testTarget = line.split()
    return int(testTarget)


def createMonkey(inputData: list[str]) -> Monkey:
    items = getItems(inputData[1])
    operation = getOperation(inputData[2])
    testNumber = getTestNumber(inputData[3])
    testTrueTarget = getTestTarget(inputData[4])
    testFalseTarget = getTestTarget(inputData[5])

    return Monkey(items, operation, testNumber, testTrueTarget, testFalseTarget)


def getProductTestNumber(allMonkeys: list[Monkey]) -> int:
    ans = 1
    for monkey in allMonkeys:
        ans *= monkey.testNumber

    return ans


def part1(data: list[str]) -> int:
    inputData: list[str] = []
    allMonkeys: list[Monkey] = []
    for line in data:
        if line == "" or line == "end":
            allMonkeys.append(createMonkey(inputData))
            inputData = []
        else:
            inputData.append(line)

    for _ in range(20):
        for monkey in allMonkeys:
            monkey.inspectItemsPart1(allMonkeys)

    ans = [monkey.inspectedTimes for monkey in allMonkeys]
    ans.sort()

    monkeyBusiness = ans[-1] * ans[-2]
    print(monkeyBusiness)
    return monkeyBusiness


def part2(data: list[str]) -> int:
    inputData: list[str] = []
    allMonkeys: list[Monkey] = []
    for line in data:
        if line == "" or line == "end":
            allMonkeys.append(createMonkey(inputData))
            inputData = []
        else:
            inputData.append(line)

    productTestNumber = getProductTestNumber(allMonkeys)

    for _ in range(10000):
        for monkey in allMonkeys:
            monkey.inspectItemsPart2(allMonkeys, productTestNumber)

    ans = [monkey.inspectedTimes for monkey in allMonkeys]
    ans.sort()

    monkeyBusiness = ans[-1] * ans[-2]

    print(monkeyBusiness)
    return monkeyBusiness


def test_passing():
    with open("test.txt", "r") as f:
        data = f.read().splitlines()
        # assert part1(data) == 10605
        assert part2(data) == 2713310158
        f.close()


with open("day11.txt", "r") as f:
    data = f.read().splitlines()

    # part1(data)

    part2(data)

    test_passing()

    f.close()
