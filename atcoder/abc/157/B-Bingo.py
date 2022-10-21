A = [[0 for x in range(3)] for y in range(3)]
i = 0
while i < 3:
    A[i] = list(map(int, input().split()))
    i += 1


N = int(input())
i = 0
while i < N:
    b = int(input())

    j = 0
    while j < 3:
        if b in A[j]:
            A[j][A[j].index(b)] = 0

        j += 1

    i += 1

ans = "No"
i = 0
while i < 3:
    if A[i][0] + A[i][1] + A[i][2] == 0:
        ans = "Yes"

    if A[0][i] + A[1][i] + A[2][i] == 0:
        ans = "Yes"

    i += 1

if A[0][0] + A[1][1] + A[2][2] == 0:
    ans = "Yes"

if A[0][2] + A[1][1] + A[2][0] == 0:
    ans = "Yes"

print(ans)
