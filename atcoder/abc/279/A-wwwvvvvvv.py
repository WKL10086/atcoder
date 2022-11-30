S = input()

ans = 0
for ele in S:
    if ele == "v":
        ans += 1
    elif ele == "w":
        ans += 2

print(ans)
