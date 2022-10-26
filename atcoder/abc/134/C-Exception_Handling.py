N = int(input())
A = [0 for _ in range(N)]

biggest = 0
biggest_2nd = 0

for i in range(N):
    A[i] = int(input())

    if i == 0:
        continue
    elif i == 1:
        if A[0] > A[1]:
            biggest = A[0]
            biggest_2nd = A[1]
        else:
            biggest_2nd = A[0]
            biggest = A[1]
    else:
        if A[i] >= biggest:
            biggest_2nd = biggest
            biggest = A[i]
        elif A[i] >= biggest_2nd:
            biggest_2nd = A[i]

for i in range(N):
    if A[i] == biggest:
        print(biggest_2nd)
    else:
        print(biggest)
