N = int(input())

city = {}

for i in range(N):
    S, P = input().split()
    P = int(P)

    if S not in city:
        city[S] = [(P, i + 1)]
    else:
        city[S].append((P, i + 1))
        city[S].sort(key=lambda tup: tup[0], reverse=True)

city = dict(sorted(city.items()))

for key in city:
    for ele in city[key]:
        print(ele[1])
