A = int(input())
B = int(input())
C = int(input())
X = int(input())


ans = 0

i = 0
while i <= A:

    j = 0
    while j <= B:

        k = 0
        while k <= C:
            temp = i * 500 + j * 100 + k * 50
            if X == temp:
                ans += 1
            k += 1

        j += 1

    i += 1

print(ans)
