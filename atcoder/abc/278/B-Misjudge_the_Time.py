H, M = input().split()


ans = ""
while True:
    if len(H) == 1:
        H = "0" + H
    if len(M) == 1:
        M = "0" + M

    tempH = int(H[0] + M[0])
    tempM = int(H[1] + M[1])

    if tempH <= 23 and tempM <= 59:
        ans = H + " " + M
        print(ans)
        break
    else:
        M = int(M) + 1
        H = int(H)
        if M == 60:
            M = 0
            H += 1

        if H == 24:
            H = 0

        M = str(M)
        H = str(H)
