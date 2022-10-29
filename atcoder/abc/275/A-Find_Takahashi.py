N = int(input())
H = list(map(int, input().split()))

ans = 0
highest = 0

i = 0
while i < N:
    if H[i] > highest:
        highest = H[i]
        ans = i

    i += 1

print(ans + 1)
