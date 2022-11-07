N, M = map(int, input().split())

city = [set() for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    city[A - 1].add(B)
    city[B - 1].add(A)


for ele in city:
    ans = list(ele)
    ans.sort()
    ans.insert(0, len(ans))
    print(" ".join(map(str, ans)))
