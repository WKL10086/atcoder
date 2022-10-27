A, B = map(int, input().split())

ans = B // 100 - A // 100 + 1

if int(str(A)[1] + str(A)[0]) < int(str(A)[3] + str(A)[4]):
    ans -= 1

if int(str(B)[1] + str(B)[0]) > int(str(B)[3] + str(B)[4]):
    ans -= 1


print(ans)
