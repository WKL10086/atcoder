with open("input.txt", "r") as f:
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
