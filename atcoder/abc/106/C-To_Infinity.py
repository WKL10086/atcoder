S = input()
K = int(input())

ans = 1
i = 0
while i < K:
    if S[i] != "1":
        ans = int(S[i])
        break
    i += 1

print(ans)
