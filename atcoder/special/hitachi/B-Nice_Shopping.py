A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


ticket = list(map(int, input().split()))
ans = a[ticket[0] - 1] + b[ticket[1] - 1] - ticket[2]

i = 1
while i < M:
    ticket = list(map(int, input().split()))
    ans = min(ans, a[ticket[0] - 1] + b[ticket[1] - 1] - ticket[2])
    i += 1

a.sort()
b.sort()
ans = min(ans, a[0] + b[0])

print(ans)
