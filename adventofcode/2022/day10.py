class CPU:
    def __init__(self):
        self.data = 1
        self.cycle = [1]
        self.currentCRT = ""
        self.allCRTs = []

    def action_noop(self):
        self.cycle.append(self.data)

    def action_addx(self, value):
        self.cycle.append(self.data)
        self.data += value
        self.cycle.append(self.data)

    def sumOfStrength(self) -> int:
        strength = 0
        target = [20, 60, 100, 140, 180, 220]
        for ele in target:
            strength += ele * self.cycle[ele - 1]
        return strength

    def computeCRT(self) -> list[str]:
        for i in range(len(self.cycle)):
            spritePosition = self.cycle[i]
            if len(self.currentCRT) in [
                spritePosition - 1,
                spritePosition,
                spritePosition + 1,
            ]:
                self.currentCRT += "#"
            else:
                self.currentCRT += "."

            if len(self.currentCRT) == 40:
                self.allCRTs.append(self.currentCRT)
                self.currentCRT = ""

        return self.allCRTs


def part1(data: list[str]) -> int:
    cpu = CPU()
    for lines in data:
        command = lines.split(" ")
        if command[0] == "noop":
            cpu.action_noop()
        elif command[0] == "addx":
            value = int(command[1])
            cpu.action_addx(value)

    ans = cpu.sumOfStrength()

    print(len(cpu.cycle))
    # print(ans)
    return ans


def part2(data: list[str]) -> list[str]:
    cpu = CPU()
    for lines in data:
        command = lines.split(" ")
        if command[0] == "noop":
            cpu.action_noop()
        elif command[0] == "addx":
            value = int(command[1])
            cpu.action_addx(value)

    allCRTs = cpu.computeCRT()

    for ele in allCRTs:
        print(ele, end="\n")

    return allCRTs


def test_passing():
    with open("test.txt", "r") as f:
        data = f.read().splitlines()
        # assert part1(data) == 13140
        # assert part2(data) == [
        #     "##..##..##..##..##..##..##..##..##..##..",
        #     "###...###...###...###...###...###...###.",
        #     "####....####....####....####....####....",
        #     "#####.....#####.....#####.....#####.....",
        #     "######......######......######......####",
        #     "#######.......#######.......#######.....",
        # ]
        f.close()


with open("day10.txt", "r") as f:
    data = f.read().splitlines()

    # part1(data)

    # ans = BJFRHRFU from actual output
    ###....##.####.###..#..#.###..####.#..#.
    # ..#....#.#....#..#.#..#.#..#.#....#..#.
    ###.....#.###..#..#.####.#..#.###..#..#.
    # ..#....#.#....###..#..#.###..#....#..#.
    # ..#.#..#.#....#.#..#..#.#.#..#....#..#.
    ###...##..#....#..#.#..#.#..#.#.....##..
    part2(data)

    test_passing()

    f.close()
