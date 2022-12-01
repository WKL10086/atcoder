with open("input.txt", "r") as f:
    data = f.read().splitlines()

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

    f.close()
