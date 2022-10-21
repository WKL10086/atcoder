N, K = map(int, input().split())

ans = 0

if N != K:
    x = N % K
    ans = min(x, K - x)


print(ans)
