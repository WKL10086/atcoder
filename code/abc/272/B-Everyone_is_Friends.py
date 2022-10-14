N, M = input().split()

pplDict = {}

i = 0
while i < int(M):
    party = input().split()
    k = party.pop(0)

    j = 0
    while j < int(k):
        if party[j] in pplDict:
            pplDict[party[j]].update(party)
        else:
            pplDict[party[j]] = set(party)

        j += 1

    i += 1

out = True

for x in pplDict.values():
    if len(x) != int(N):
        out = False


if out:
    print("Yes")
else:
    print("No")
