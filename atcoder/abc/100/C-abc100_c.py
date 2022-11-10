N = int(input())
A = list(map(int, input().split()))

ans = 0
for ele in A:
    while ele % 2 == 0:
        ans += 1
        ele /= 2

print(ans)
