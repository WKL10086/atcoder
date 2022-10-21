N = int(input())
A = list(map(int, input().split()))
ans = [0 for _ in range(N)]

i = 0
while i < N:
    ans[A[i] - 1] = str(i + 1)
    i += 1

print(" ".join(ans))
