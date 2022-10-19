X, K = map(int, input().split())

i = 1
while i <= K:
    if X == 0:
        break
    else:
        X += 1
        X = round(X, i * -1)
        i += 1

print(X)
