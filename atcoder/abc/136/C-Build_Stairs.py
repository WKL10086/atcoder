N = int(input())
H = list(map(int, input().split()))

ans = True
i = 0
while i < len(H):
    if i == 0:
        H[i] -= 1
    else:
        if H[i] - 1 >= H[i - 1]:
            H[i] -= 1
        elif H[i] < H[i - 1]:
            ans = False
            break

    i += 1

if ans:
    print("Yes")
else:
    print("No")
