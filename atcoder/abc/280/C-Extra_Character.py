S = input()
T = input()

ans = 0
end = True
for i in range(len(S)):
    if S[i] != T[i]:
        ans = i + 1
        end = False
        break

if end:
    ans = len(T)


print(ans)
