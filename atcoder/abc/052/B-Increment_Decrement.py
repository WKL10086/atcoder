N = int(input())
S = input()

x = 0
ans = 0

for ele in S:
    if ele == "I":
        x += 1
    else:
        x -= 1

    ans = max(ans, x)

print(ans)
