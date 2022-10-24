X = int(input())


def checkPrime(x):
    isPrime = True
    for i in range(3, int(x**0.5) + 1, 2):
        if X % i == 0:
            isPrime = False
            break

    return isPrime


if X % 2 == 0 and X != 2:
    X += 1

while True:
    if checkPrime(X):
        print(X)
        break
    else:
        X += 2
