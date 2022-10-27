N = int(input())
L = [0 for _ in range(N + 1)]

L[0] = 2
L[1] = 1

i = 2
while i < N + 1:
    L[i] = L[i - 1] + L[i - 2]

    i += 1

print(L[len(L) - 1])
