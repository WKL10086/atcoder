A, B = map(int, input().split())

ans = str(round(B / A, 3))

while len(ans) < 5:
    ans = ans + "0"

print(ans)
