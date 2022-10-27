w = input()

letter = {}

for ele in w:
    if ele not in letter:
        letter[ele] = 1
    else:
        letter[ele] += 1

isEven = True
for ele in letter:
    if letter[ele] % 2 != 0:
        isEven = False

if isEven:
    print("Yes")
else:
    print("No")
