# TODO: exactly one occurrence of C
S = input()

ans = "AC"

if S[0] != "A":
    ans = "WA"
else:
    if S[2] != S[-2] and S[2] == "C":
        i = 0
        while i < len(S):
            if i == 2 or i == 0:
                i += 1
                continue
            else:
                if S[i].isupper():
                    ans = "WA"
                i += 1

    elif S[2] != S[-2] and S[-2] == "C":
        i = 0
        while i < len(S):
            if i == len(S) - 2 or i == 0:
                i += 1
                continue
            else:
                if S[i].isupper():
                    ans = "WA"
                i += 1

    else:
        ans = "WA"

print(ans)
