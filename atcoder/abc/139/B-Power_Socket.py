A, B = map(int, input().split())

if B != 1:
    if B >= A:
        counter = ((B - A) // (A - 1)) + 1
        if (B - A) % (A - 1) > 0:
            counter += 1
    else:
        counter = 1
else:
    counter = 0

print(counter)
