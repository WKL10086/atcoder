N = int(input())
K = int(input())
X = list(map(int, input().split()))

sum = 0
for ele in X:
    sum += min(ele * 2, abs(ele - K) * 2)

print(sum)
