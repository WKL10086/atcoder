N, L = map(int, input().split())

ans = []
for i in range(N):
    S = input()
    ans.append(S)

ans.sort()
print("".join(ans))
