with open("input.txt", "r") as f:
    data = f.read().splitlines()

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

    f.close()
