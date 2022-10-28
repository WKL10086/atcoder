N = int(input())
B = list(map(int, input().split()))


A = [0 for _ in range(N)]

A[0] = B[0]
B.append(B[len(B) - 1])

i = 1
while i < N:
    A[i] = min(B[i], B[i - 1])

    i += 1

print(sum(A))
