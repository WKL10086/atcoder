# TODO: TLE
N = int(input())

counter = 0


def recursiveFunc(n):
    global counter

    if n == 0:
        counter += 1
    else:
        recursiveFunc(int(n / 2))
        recursiveFunc(int(n / 3))


recursiveFunc(N)
print(counter)
