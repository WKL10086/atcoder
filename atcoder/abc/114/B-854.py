S = input()


i = 0
while (i + 2) < len(S):
    if i == 0:
        ans = abs(int(S[i] + S[i + 1] + S[i + 2]) - 753)
    else:
        ans = min(ans, abs(int(S[i] + S[i + 1] + S[i + 2]) - 753))
    i += 1


print(ans)
