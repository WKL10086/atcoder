N = int(input())
A = list(map(int, input().split()))

rabbits = dict()
ans = 0

i = 0
while i < len(A):
    rabbits[i + 1] = A[i]

    if A[i] in rabbits:
        if rabbits[A[i]] == i + 1:
            ans += 1

    i += 1

print(ans)
