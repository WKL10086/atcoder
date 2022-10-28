import math

A, B = map(int, input().split())

price = []
for i in range(math.ceil(A / 0.08), math.floor((A + 1) / 0.08) + 1):
    price.append(i)

i = math.ceil(B / 0.1)
while i < math.floor((B + 1) / 0.1) + 1:
    if i in price:
        print(i)
        break

    i += 1

if i == math.floor((B + 1) / 0.1) + 1:
    print(-1)
