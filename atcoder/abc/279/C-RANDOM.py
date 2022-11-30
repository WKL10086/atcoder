H, W = map(int, input().split())

S = [[] for _ in range(W)]
T = [[] for _ in range(W)]

for _ in range(H):
    s = list(input())
    for i in range(W):
        S[i].append(s[i])

for _ in range(H):
    t = list(input())
    for i in range(W):
        T[i].append(t[i])

S.sort()
T.sort()
if S == T:
    print("Yes")
else:
    print("No")
