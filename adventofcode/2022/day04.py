def part1(data: list[str]):
    ans = 0
    for line in data:
        firstElf, secondElf = line.split(",")
        firstLower, firstUpper = map(int, firstElf.split("-"))
        secondLower, secondUpper = map(int, secondElf.split("-"))

        if (firstLower <= secondLower and firstUpper >= secondUpper) or (
            secondLower <= firstLower and secondUpper >= firstUpper
        ):
            ans += 1

    print(ans)


def part2(data: list[str]):
    ans = 0
    for line in data:
        firstElf, secondElf = line.split(",")
        firstLower, firstUpper = map(int, firstElf.split("-"))
        secondLower, secondUpper = map(int, secondElf.split("-"))

        if (firstLower <= secondLower and firstUpper >= secondLower) or (
            secondLower <= firstLower and secondUpper >= firstLower
        ):
            ans += 1

    print(ans)


# with open("test.txt", "r") as f:
with open("day04.txt", "r") as f:
    data = f.read().splitlines()

    # part1(data)

    part2(data)

    f.close()
