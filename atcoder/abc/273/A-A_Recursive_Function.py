N = int(input())


def add(n):
    if n == 0:
        return 1
    else:
        return n * add(n - 1)


sum = add(N)

print(sum)
