S = input()

stact = []

for ele in S:
    if len(stact) == 0:
        stact.append(ele)
    else:
        if ele == "1":
            if stact[-1] == "0":
                stact.pop(-1)
            else:
                stact.append(ele)
        else:
            if stact[-1] == "1":
                stact.pop(-1)
            else:
                stact.append(ele)

ans = len(S) - len(stact)
print(ans)
