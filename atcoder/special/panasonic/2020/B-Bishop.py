H, W = map(int, input().split())

if H == 1 or W == 1:
    print(1)
else:
    if H % 2 == 0:
        print(H // 2 * W)
    else:
        if W % 2 == 0:
            print((H - 1) // 2 * W + (W // 2))
        else:
            print((H - 1) // 2 * W + (W // 2) + 1)
