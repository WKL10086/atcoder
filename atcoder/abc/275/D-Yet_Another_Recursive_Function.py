N = int(input())

memorisation = {}


def recursiveFunc(n):
    global memorisation

    if n in memorisation:
        return memorisation[n]

    if n == 0:
        result = 1
    else:
        result = recursiveFunc(int(n / 2)) + recursiveFunc(int(n / 3))

    memorisation[n] = result
    return result


print(recursiveFunc(N))
