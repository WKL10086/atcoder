H, W = map(int, input().split())

ans = [0 for _ in range(W)]

i = 0
while i < H:
    c = input()

    j = 0
    while j < W:
        if c[j] == "#":
            ans[j] += 1
        j += 1
    i += 1

ans = map(str, ans)
print(" ".join(ans))
