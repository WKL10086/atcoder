S = input()
S = set(S)

char = "abcdefghijklmnopqrstuvwxyz"

i = 0
while i < len(char):
    if char[i] in S:
        i += 1
    else:
        break

if i == 26:
    print("None")
else:
    print(char[i])
