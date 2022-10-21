import math


tax = 1.08
N = int(input())

down = math.floor(N / tax)
up = math.ceil(N / tax)

if math.floor(down * tax) == N:
    print(down)
elif math.floor(up * tax) == N:
    print(up)
else:
    print(":(")
