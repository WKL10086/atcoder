# ans 1
N, Q = map(int, input().split())
pairs = set()

for _ in range(Q):
    T, A, B = map(int, input().split())

    if T == 1:
        pair = str(A) + " " + str(B)
        pairs.add(pair)
    elif T == 2:
        pair = str(A) + " " + str(B)
        pairs.discard(pair)
    elif T == 3:
        pairA = str(A) + " " + str(B)
        pairB = str(B) + " " + str(A)

        if pairA in pairs and pairB in pairs:
            print("Yes")
        else:
            print("No")
