N = int(input())
cards = set()
ans = True

for i in range(N):
    S = input()
    if (S[0] == "H" or S[0] == "D" or S[0] == "C" or S[0] == "S") and (
        S[1] == "A"
        or S[1] == "2"
        or S[1] == "3"
        or S[1] == "4"
        or S[1] == "5"
        or S[1] == "6"
        or S[1] == "7"
        or S[1] == "8"
        or S[1] == "9"
        or S[1] == "T"
        or S[1] == "J"
        or S[1] == "Q"
        or S[1] == "K"
    ):
        cards.add(S)
    else:
        ans = False
        break

if len(cards) != N:
    ans = False

if ans:
    print("Yes")
else:
    print("No")
