N = int(input())
A = list(map(int, input().split()))

ans = 0
counter = 1
for ele in A:
    if ele != counter:
        ans += 1
    else:
        counter += 1

if ans == len(A):
    print(-1)
else:
    print(ans)
