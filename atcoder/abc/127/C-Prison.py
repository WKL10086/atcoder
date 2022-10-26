N, M = map(int, input().split())


L, R = map(int, input().split())

i = 1
while i < M:
    tempL, tempR = map(int, input().split())
    L = max(L, tempL)
    R = min(R, tempR)

    i += 1

if L > R:
    print(0)
else:
    print(R - L + 1)
