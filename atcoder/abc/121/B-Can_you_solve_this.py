N, M, C = map(int, input().split())
B = list(map(int, input().split()))
ans = 0
i = 0
while i < N:
    A = list(map(int, input().split()))

    j = 0
    sum = 0
    while j < M:
        sum += A[j] * B[j]
        j += 1

    if sum + C > 0:
        ans += 1

    i += 1

print(ans)
