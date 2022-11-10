import math

N = int(input())
upper = int(math.sqrt(N)) + 1

ans = math.inf
for i in range(1, upper):
    if N % i == 0:
        ans = min(ans, i + int(N / i) - 2)

print(ans)
