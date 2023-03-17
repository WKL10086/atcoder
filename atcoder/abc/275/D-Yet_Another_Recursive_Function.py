N = int(input())

memorization = {}


def recursiveFunc(n):
    global memorization

    if n in memorization:
        return memorization[n]

    if n == 0:
        result = 1
    else:
        result = recursiveFunc(int(n / 2)) + recursiveFunc(int(n / 3))

    memorization[n] = result
    return result


print(recursiveFunc(N))
