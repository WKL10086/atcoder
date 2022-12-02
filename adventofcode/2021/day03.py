import copy


def part1(data: list[str]):
    num_0 = [0 for _ in range(len(data[0]))]
    num_1 = [0 for _ in range(len(data[0]))]

    for ele in data:
        i = 0
        while i < len(ele):
            if ele[i] == "0":
                num_0[i] += 1
            else:
                num_1[i] += 1
            i += 1

    gamma = ""
    epsilon = ""
    i = 0
    while i < len(num_0):
        if num_0[i] > num_1[i]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
        i += 1

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print(gamma * epsilon)


def part2(data: list[str]):
    remaining = [ele for ele in data]

    for i in range(len(data[0])):
        if len(remaining) == 1:
            break

        num_0 = 0
        num_1 = 0

        for ele in remaining:
            if ele[i] == "0":
                num_0 += 1
            else:
                num_1 += 1

        if num_0 > num_1:
            remaining = [ele for ele in remaining if ele[i] == "0"]
        elif num_0 == num_1:
            remaining = [ele for ele in remaining if ele[i] == "1"]
        elif num_0 < num_1:
            remaining = [ele for ele in remaining if ele[i] == "1"]

    oxygen = remaining[0]

    remaining = [ele for ele in data]

    for i in range(len(data[0])):
        if len(remaining) == 1:
            break

        num_0 = 0
        num_1 = 0

        for ele in remaining:
            if ele[i] == "0":
                num_0 += 1
            else:
                num_1 += 1

        if num_0 > num_1:
            remaining = [ele for ele in remaining if ele[i] == "1"]
        elif num_0 == num_1:
            remaining = [ele for ele in remaining if ele[i] == "0"]
        elif num_0 < num_1:
            remaining = [ele for ele in remaining if ele[i] == "0"]

    carbonDioxide = remaining[0]

    oxygen = int(oxygen, 2)
    carbonDioxide = int(carbonDioxide, 2)

    print(oxygen * carbonDioxide)


with open("day03.txt", "r") as f:
    data = f.read().splitlines()

    part1(data)

    part2(data)

    f.close()
