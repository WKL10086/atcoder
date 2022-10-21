import math


A, B = input().split()
x = int(A + B)

if math.sqrt(x) % 1 == 0:
    print("Yes")
else:
    print("No")
