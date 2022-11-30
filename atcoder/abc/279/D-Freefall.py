import math


A, B = map(int, input().split())

x = (2 * B / A) ** (-2 / 3)

x = round(x)

ans = math.inf

for i in range(x - 1, x + 2):
    if i <= 0:
        ans = min(ans, A)
    else:
        y = B * (i - 1) + A / (math.sqrt(i))
        ans = min(ans, y)

print(ans)
