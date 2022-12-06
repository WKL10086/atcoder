def part1(data: list[str]):
    for line in data:
        start = 0
        while start + 4 <= len(line):
            temp = line[start : start + 4]
            if len(set(temp)) != len(temp):
                start += 1
            else:
                print(start + 4)
                break


def part2(data: list[str]):
    for line in data:
        start = 0
        while start + 14 <= len(line):
            temp = line[start : start + 14]
            if len(set(temp)) != len(temp):
                start += 1
            else:
                print(start + 14)
                break


# with open("test.txt", "r") as f:
with open("day06.txt", "r") as f:
    data = f.read().splitlines()

    # part1(data)

    part2(data)

    f.close()
