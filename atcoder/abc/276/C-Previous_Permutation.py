# Cantor Expansion
import math

N = int(input())
P = list(map(int, input().split()))

pOrder = 1

i = 0
while i < N:
    tempP = [x for x in P[0:i] if x < P[i]]
    pOrder += math.factorial(N - 1 - i) * (P[i] - len(tempP) - 1)
    i += 1


ans = []
ansOrder = 1
notUsedTemp = [x + 1 for x in reversed(range(N))]

while len(notUsedTemp) != 0:
    for ele in notUsedTemp:
        smaller = [x for x in ans if x < ele]
        tempOrder = ansOrder + math.factorial(N - 1 - len(ans)) * (
            ele - len(smaller) - 1
        )
        if tempOrder > pOrder - 1:
            continue
        else:
            ans.append(ele)
            ansOrder = tempOrder
            notUsedTemp.remove(ele)
            break

print(" ".join(map(str, ans)))
