import math

N = int(input())
A = list(map(int, input().split()))

total = sum(A)
temp = 0
ans = total - temp

i = 0
while i < len(A) - 1:
    temp += A[i]
    total -= A[i]
    ans = min(ans, abs(total - temp))
    i += 1

print(ans)
