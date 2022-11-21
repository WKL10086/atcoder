# TODO: wrong ans
N = int(input())
A = list(map(int, input().split()))
Q = int(input())


assigned = False
assignValue = 0
temp = dict()

for _ in range(Q):
    Query = list(map(int, input().split()))

    if assigned:
        if Query[0] == 1:
            assignValue = Query[1]
        elif Query[0] == 2:
            if Query[1] in temp:
                temp[Query[1]] += Query[2]
            else:
                temp[Query[1]] = Query[2]
        elif Query[0] == 3:
            if Query[1] in temp:
                print(temp[Query[1]] + assignValue)
            else:
                print(assignValue)
    else:
        if Query[0] == 1:
            assigned = True
            assignValue = Query[1]
        elif Query[0] == 2:
            A[Query[1] - 1] += Query[2]
        elif Query[0] == 3:
            print(A[Query[1] - 1])
