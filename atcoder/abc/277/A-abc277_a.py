N, X = map(int, input().split())
P = list(map(int, input().split()))

counter = 0
while counter < len(P):
    if P[counter] == X:
        break
    counter += 1

print(counter + 1)
