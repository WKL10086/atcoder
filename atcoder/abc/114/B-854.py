S = input()


i = 0
while (i + 2) < len(S):
    if i == 0:
        ans = int(S[i] + S[i + 1] + S[i + 2]) - 753
    else:
        ans = min(ans, abs(int(S[i] + S[i + 1] + S[i + 2]) - 753))
    i += 1

i = 0
while (i + 3) < len(S):
    ans = min(ans, abs(int(S[i] + S[i + 1] + S[i + 2] + S[i + 3]) - 753))
    i += 1

print(ans)
