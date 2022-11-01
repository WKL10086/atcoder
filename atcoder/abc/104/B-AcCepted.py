S = input()

ans = "AC"

if S[0] != "A":
    ans = "WA"

i = 2
counter = 0
while i < len(S) - 1:
    if S[i] == "C":
        counter += 1
    i += 1

if counter != 1:
    ans = "WA"


counter = 0
for ele in S:
    if ele.isupper():
        counter += 1
if counter != 2:
    ans = "WA"

print(ans)
