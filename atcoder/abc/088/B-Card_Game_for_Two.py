N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
i = 0
Alice = 0
Bob = 0
while i < len(A):
    if i % 2 == 0:
        Alice += A[i]
    else:
        Bob += A[i]

    i += 1

print(Alice - Bob)
