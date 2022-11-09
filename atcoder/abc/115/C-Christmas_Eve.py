N, K = map(int, input().split())
trees = []

for _ in range(N):
    trees.append(int(input()))

trees.sort()

ans = trees[K - 1] - trees[0]

lower = 1
upper = K
while upper < len(trees):
    ans = min(ans, trees[upper] - trees[lower])
    lower += 1
    upper += 1

print(ans)
