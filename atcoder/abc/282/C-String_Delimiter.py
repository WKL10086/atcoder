N = int(input())
S = input()

ans = ""
enclosed = False
for ele in S:
    if ele == '"':
        enclosed = not enclosed
        ans += '"'
        continue

    if not enclosed and ele == ",":
        ans += "."
    else:
        ans += ele

print(ans)
