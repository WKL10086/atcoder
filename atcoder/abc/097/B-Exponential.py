X = int(input())
upper = int(X ** (1 / 2))
ans = 1

temp = [i for i in range(2, upper + 1)]
for i in temp:
    counter = i
    while counter * i <= X:
        counter *= i
    ans = max(counter, ans)

print(ans)
