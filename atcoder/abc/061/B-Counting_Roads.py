N, M = map(int, input().split())

city = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())

    city[a - 1].append(b - 1)
    city[b - 1].append(a - 1)

for ele in city:
    print(len(ele))
