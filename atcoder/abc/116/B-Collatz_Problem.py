s = int(input())
temp = set()
counter = 1


def collatzProblem(x):

    if x % 2 == 0:
        return x // 2
    else:
        return 3 * x + 1


while s not in temp:
    temp.add(s)
    s = collatzProblem(s)
    counter += 1

print(counter)
