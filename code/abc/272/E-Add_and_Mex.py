N, M = input().split()
N = int(N)
M = int(M)
A = input().split()
A = list(map(int, A))

mex = 1

counter = 0
while counter < M:
    if mex == 0:
        print(0)
    else:
        i = 0
        while i < N:
            A[i] = A[i] + i + 1
            i += 1

        filterd = [ele for ele in A if ele >= 0]
        filterd.sort()

        j = 0
        while j < N:
            if j not in filterd:
                mex = j
            j += 1

    print(mex)
    counter += 1
