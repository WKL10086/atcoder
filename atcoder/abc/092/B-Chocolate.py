N = int(input())
D, X = map(int, input().split())


i = 0
while i < N:
    A = int(input())
    X += ((D - 1) // A) + 1
    i += 1

print(X)
