def part1():
    with open("day02.txt", "r") as f:
        data = f.read().splitlines()

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

        f.close()


def part2():
    with open("day02.txt", "r") as f:
        data = f.read().splitlines()

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

        f.close()
