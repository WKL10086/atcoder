import math

# dfs or Cantor Expansion

# Cantor Expansion
def cantorExpansion():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    # current case
    pOrder = 1
    qOrder = 1

    # cal prev case
    i = 0
    while i < N:
        tempP = [x for x in P[0:i] if x < P[i]]
        pOrder += math.factorial(N - 1 - i) * (P[i] - len(tempP) - 1)

        tempQ = [x for x in Q[0:i] if x < Q[i]]
        qOrder += math.factorial(N - 1 - i) * (Q[i] - len(tempQ) - 1)

        i += 1

    print(abs(pOrder - qOrder))


cantorExpansion()
