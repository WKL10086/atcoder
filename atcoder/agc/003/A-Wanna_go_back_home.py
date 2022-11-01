S = input()

Ncounter = True if "N" in S else False
Scounter = True if "S" in S else False
Ecounter = True if "E" in S else False
Wcounter = True if "W" in S else False


if (Ncounter == Scounter) and (Ecounter == Wcounter):
    print("Yes")
else:
    print("No")
