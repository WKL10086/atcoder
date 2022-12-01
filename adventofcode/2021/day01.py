def part1(data: list[str]):
    N = len(data)

    prev = 0
    counter = 0
    for i in range(N):
        current = int(data[i])

        if i == 0:
            prev = current
            continue
        else:
            if current > prev:
                counter += 1

            prev = current

    print(counter)


def part2(data: list[str]):
    data = list(map(int, data))

    N = len(data)

    prev = data[0] + data[1] + data[2]
    counter = 0

    i = 1
    while i + 2 < N:
        current = data[i] + data[i + 1] + data[i + 2]

        if current > prev:
            counter += 1

        prev = current

        i += 1

    print(counter)


with open("day01.txt", "r") as f:
    data = f.read().splitlines()

    part1(data)

    part2(data)

    f.close()
