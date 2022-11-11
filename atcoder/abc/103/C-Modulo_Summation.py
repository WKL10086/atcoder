N = int(input())
A = list(map(int, input().split()))

ans = sum(A) - len(A)

print(ans)
