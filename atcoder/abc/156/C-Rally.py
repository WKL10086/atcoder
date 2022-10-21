from statistics import mean


N = int(input())
X = list(map(int, input().split()))

avg = round(mean(X))

sum = 0
for ele in X:
    sum += abs(ele - avg) ** 2

print(sum)
