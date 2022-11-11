N = int(input())

ans = 1
counter = 1
while counter < N + 1:
    temp = counter % 1000000007
    ans *= temp
    ans %= 1000000007
    counter += 1

print(ans)
