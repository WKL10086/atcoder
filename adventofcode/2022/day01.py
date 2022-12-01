def part1(data: list[str]):
    ans = 0
    currentTotal = 0

    for ele in data:
        if ele != "":
            calories = int(ele)
            currentTotal += calories
            ans = max(ans, currentTotal)
        else:
            currentTotal = 0

    ans = max(ans, currentTotal)  # check the last one

    print(ans)


def part2(data: list[str]):
    elf = []
    currentTotal = 0

    for ele in data:
        if ele != "":
            calories = int(ele)
            currentTotal += calories
        else:
            elf.append(currentTotal)
            currentTotal = 0

    elf.append(currentTotal)  # add the last one
    elf.sort()

    print(elf[-1] + elf[-2] + elf[-3])


with open("day01.txt", "r") as f:
    data = f.read().splitlines()

    part1(data)

    part2(data)

    f.close()
