S = input()

ans = 0
counter = 0
i = 0
while i < len(S):
    if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
        counter += 1
        ans = max(counter, ans)
    else:
        counter = 0

    i += 1

print(ans)
