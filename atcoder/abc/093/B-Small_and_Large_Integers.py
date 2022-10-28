A, B, K = map(int, input().split())

ans = set()

i = A
while i < min(A + K, B):
    ans.add(i)
    i += 1

i = max(B - K + 1, A)
counter = 0
while i < B + 1:
    if counter >= K:
        break

    ans.add(i)
    i += 1
    counter += 1

ans = list(ans)
ans.sort()

for ele in ans:
    print(ele)
