def part1(data: list[str]):
    horizontal = 0
    depth = 0

    for ele in data:
        command, num = ele.split()
        num = int(num)

        if command == "forward":
            horizontal += num
        elif command == "down":
            depth += num
        elif command == "up":
            depth -= num

    print(horizontal * depth)


def part2(data: list[str]):
    horizontal = 0
    depth = 0
    aim = 0

    for ele in data:
        command, num = ele.split()
        num = int(num)

        if command == "forward":
            horizontal += num
            depth += aim * num
        elif command == "down":
            aim += num
        elif command == "up":
            aim -= num

    print(horizontal * depth)


with open("day02.txt", "r") as f:
    data = f.read().splitlines()

    part1(data)

    part2(data)

    f.close()
