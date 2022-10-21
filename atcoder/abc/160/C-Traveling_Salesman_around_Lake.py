K, N = map(int, input().split())
A = list(map(int, input().split()))

i = len(A) - 1
temp = A[len(A) - 1] - K
while i > 0:
    A[i] = abs(A[i] - A[i - 1])
    i -= 1

A[0] = abs(A[0] - temp)

A.sort()
A.pop()
print(sum(A))
