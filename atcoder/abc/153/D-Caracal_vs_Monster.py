H = int(input())

monster = 1
counter = 0

while H != 0:
    if H == 1:
        counter += monster

        H = 0
    else:
        counter += monster

        H //= 2
        monster *= 2

print(counter)
