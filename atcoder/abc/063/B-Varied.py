S = input()
test = set()

for ele in S:
    test.add(ele)

if len(test) == len(S):
    print("yes")
else:
    print("no")
