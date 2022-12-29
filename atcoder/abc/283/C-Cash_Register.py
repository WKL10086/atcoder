S = input()

ans = 0

i = 0
while i < len(S):
    ans += 1

    if S[i] == "0":
        if i + 1 < len(S) and S[i + 1] == "0":
            i += 1

    i += 1

print(ans)
