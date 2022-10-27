N, M = map(int, input().split())
foods = [0 for _ in range(M)]

for _ in range(N):
    pplLoved = list(map(int, input().split()))

    j = 1
    while j < len(pplLoved):
        foods[pplLoved[j] - 1] += 1
        j += 1

ans = 0
for ele in foods:
    if ele == N:
        ans += 1

print(ans)
