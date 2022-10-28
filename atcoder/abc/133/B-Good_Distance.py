from dis import dis
import math

N, D = map(int, input().split())

points = [[0 for _ in range(D)] for _ in range(N)]

for i in range(N):
    points[i] = list(map(int, input().split()))

ans = 0

i = 0
while i < N:
    j = i + 1
    while j < N:

        sum = 0
        k = 0
        while k < D:
            sum += (points[i][k] - points[j][k]) ** 2

            k += 1

        distance = math.sqrt(sum)
        if distance.is_integer():
            ans += 1

        j += 1
    i += 1

print(ans)
