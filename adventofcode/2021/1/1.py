with open("input.txt", "r") as f:
    data = f.read().splitlines()

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

    f.close()
