def part1(data: list[str]):
    score = 0

    for ele in data:
        oppo, me = ele.split(" ")

        if me == "X":
            score += 1
        elif me == "Y":
            score += 2
        elif me == "Z":
            score += 3

        if oppo == "A":
            if me == "X":
                score += 3
            elif me == "Y":
                score += 6
            elif me == "Z":
                score += 0
        elif oppo == "B":
            if me == "X":
                score += 0
            elif me == "Y":
                score += 3
            elif me == "Z":
                score += 6
        elif oppo == "C":
            if me == "X":
                score += 6
            elif me == "Y":
                score += 0
            elif me == "Z":
                score += 3

    print(score)


def part2(data: list[str]):
    score = 0

    for ele in data:
        oppo, me = ele.split(" ")

        if me == "X":
            score += 0
        elif me == "Y":
            score += 3
        elif me == "Z":
            score += 6

        if oppo == "A":
            if me == "X":
                score += 3
            elif me == "Y":
                score += 1
            elif me == "Z":
                score += 2
        elif oppo == "B":
            if me == "X":
                score += 1
            elif me == "Y":
                score += 2
            elif me == "Z":
                score += 3
        elif oppo == "C":
            if me == "X":
                score += 2
            elif me == "Y":
                score += 3
            elif me == "Z":
                score += 1

    print(score)


with open("day02.txt", "r") as f:
    data = f.read().splitlines()

    part1(data)

    part2(data)

    f.close()
