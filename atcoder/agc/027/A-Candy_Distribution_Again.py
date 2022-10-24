N, x = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

counter = 0
while counter < len(a) and x > 0:
    x -= a[counter]
    counter += 1


if x != 0:
    print(counter - 1)
else:
    print(counter)
