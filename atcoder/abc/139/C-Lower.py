N = int(input())
H = list(map(int, input().split()))

ans = 0
counter = 0

i = 1
while i < N:
    if H[i] <= H[i - 1]:
        counter += 1
        ans = max(ans, counter)
    else:
        counter = 0

    i += 1

print(ans)
