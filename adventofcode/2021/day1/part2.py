with open("input.txt", "r") as f:
    data = f.read().splitlines()
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

    f.close()
