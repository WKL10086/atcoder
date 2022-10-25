N = int(input())
A = list(map(int, input().split()))

counter = 0
while True:
    temp = [x // 2 for x in A if x % 2 == 0]
    if len(temp) == len(A):
        A = temp
        counter += 1
    else:
        break

print(counter)
