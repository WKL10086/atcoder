crates = [[] for _ in range(9)]
crates[0] = ["B", "G", "S", "C"]
crates[1] = ["T", "M", "W", "H", "J", "N", "V", "G"]
crates[2] = ["M", "Q", "S"]
crates[3] = ["B", "S", "L", "T", "W", "N", "M"]
crates[4] = ["J", "Z", "F", "T", "V", "G", "W", "P"]
crates[5] = ["C", "T", "B", "G", "Q", "H", "S"]
crates[6] = ["T", "J", "P", "B", "W"]
crates[7] = ["G", "D", "C", "Z", "F", "T", "Q", "M"]
crates[8] = ["N", "S", "H", "B", "P", "F"]


def part1(data: list[str]):
    for line in data:
        _, num, _, start, _, end = line.split(" ")
        num = int(num)
        start = int(start) - 1
        end = int(end) - 1

        for _ in range(num):
            crates[end].append(crates[start].pop())

    for ele in crates:
        print(ele[-1], end="")


def part2(data: list[str]):
    for line in data:
        _, num, _, start, _, end = line.split(" ")
        num = int(num)
        start = int(start) - 1
        end = int(end) - 1

        temp = []
        for _ in range(num):
            temp.append(crates[start].pop())
        for _ in range(num):
            crates[end].append(temp.pop())

    for ele in crates:
        print(ele[-1], end="")


# with open("test.txt", "r") as f:
with open("day05.txt", "r") as f:
    data = f.read().splitlines()

    # part1(data)

    part2(data)

    f.close()
