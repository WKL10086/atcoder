O = input()
E = input()

ans = ""
for i in range(len(O) + len(E)):
    if i % 2 == 0:
        ans += O[i // 2]
    elif i % 2 == 1:
        ans += E[(i - 1) // 2]

print(ans)
