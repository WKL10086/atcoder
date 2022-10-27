N = int(input())
P = list(map(int, input().split()))

ans = 0

prevMin = P[0]
for ele in P:
    if ele <= prevMin:
        ans += 1
        prevMin = ele


print(ans)
