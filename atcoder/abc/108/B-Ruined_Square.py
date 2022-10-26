x1, y1, x2, y2 = map(int, input().split())
ans = [0 for _ in range(4)]

a = x2 - x1
b = y2 - y1

ans[0] = x2 - b
ans[1] = y2 + a

c = ans[0] - x2
d = ans[1] - y2

ans[2] = ans[0] - d
ans[3] = ans[1] + c

print(" ".join(map(str, ans)))
