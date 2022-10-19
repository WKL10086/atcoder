N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [set() for _ in range(M)]

i = 0
while i < N:
    if A[i] >= N:
        i += 1
        continue
    elif A[i] < 0:
        startCounter = (A[i] // (i + 1)) * -1
        endCounter = min((((A[i] - N) // (i + 1)) * -1) - 1, M)
        if startCounter > M:
            i += 1
            continue
        else:
            while startCounter <= endCounter:
                S[startCounter - 1].add(A[i] + startCounter * (i + 1))
                startCounter += 1
    else:
        startCounter = 1
        endCounter = min((N - A[i]) // (i + 1), M)
        while startCounter <= endCounter:
            S[startCounter - 1].add(A[i] + startCounter * (i + 1))
            startCounter += 1

    i += 1

i = 0
while i < len(S):
    mex = 0
    while mex in S[i]:
        mex += 1

    print(mex)
    i += 1
