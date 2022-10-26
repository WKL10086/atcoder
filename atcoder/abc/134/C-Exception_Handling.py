N = int(input())

max_1st = 0
max_2nd = 0
for i in range(N):
    A = int(input())

    if A > max_1st:
        max_2nd = max_1st
        max_1st = A

    if A == max_1st:
        print(max_2nd)
    else:
        print(max_1st)
