A, B, C = map(int, input().split())

temp = [A, B, C]
temp.sort()

ans = 0
if A % 2 != 0 and B % 2 != 0 and C % 2 != 0:
    ans = temp[0] * temp[1]


print(ans)
