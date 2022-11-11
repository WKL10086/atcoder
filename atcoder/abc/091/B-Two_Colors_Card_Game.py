N = int(input())
Blue = dict()

for i in range(N):
    s = input()
    if s in Blue:
        Blue[s] += 1
    else:
        Blue[s] = 1

M = int(input())

for i in range(M):
    t = input()
    if t in Blue:
        Blue[t] -= 1

ans = 0
for key in Blue:
    ans = max(ans, Blue[key])

print(ans)
