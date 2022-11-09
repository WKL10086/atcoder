N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 0
counter = N
i = 2
while counter > 0:
    ans += A[len(A) - i]

    i += 2
    counter -= 1

print(ans)
