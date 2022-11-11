N, M = map(int, input().split())

store = []
for _ in range(N):
    A, B = map(int, input().split())
    store.append((A, B))

store.sort()

counter = 0
ans = 0
for ele in store:
    if counter < M:
        temp = min(M, counter + ele[1])
        ans += (temp - counter) * ele[0]
        counter = temp
    else:
        break

print(ans)
