def part1(data: list[str]):
    sum = 0

    for line in data:
        firstHalf = line[: len(line) // 2]
        secondHalf = line[len(line) // 2 :]

        same = [ele for ele in firstHalf if ele in secondHalf]

        if same[0].isupper():
            sum += ord(same[0]) - 38
        else:
            sum += ord(same[0]) - 96

    print(sum)


def part2(data: list[str]):
    i = 0
    firstline = ""
    secondline = ""
    thirdline = ""
    sum = 0

    while i < len(data):
        if i % 3 == 0:
            firstline = data[i]
        elif i % 3 == 1:
            secondline = data[i]
        else:
            thirdline = data[i]

            same = [ele for ele in firstline if ele in secondline and ele in thirdline]

            if same[0].isupper():
                sum += ord(same[0]) - 38
            else:
                sum += ord(same[0]) - 96

        i += 1

    print(sum)


with open("day03.txt", "r") as f:
    data = f.read().splitlines()

    part1(data)

    part2(data)

    f.close()
