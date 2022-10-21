A, B, C = map(int, input().split())


counter = 0
while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    tempA = B // 2 + C // 2
    tempB = A // 2 + C // 2
    tempC = A // 2 + B // 2
    A = tempA
    B = tempB
    C = tempC
    counter += 1

    if A == B == C:
        counter = -1
        break

print(counter)
