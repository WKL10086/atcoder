N, M = input().split()
N = int(N)
M = int(M)
A = input().split()
A = list(map(int, A))

mex = 0

counter = 0
while counter < M:
    i = 0
    while i < N:
        A[i] = A[i] + i + 1
        i += 1

    filtered = [ele for ele in A if ele >= 0]
    filtered.sort()

    j = 0
    while j < N:
        if j not in filtered:
            mex = j
            break
        j += 1

    print(mex)
    counter += 1
