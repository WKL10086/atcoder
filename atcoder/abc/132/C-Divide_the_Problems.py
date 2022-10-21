N = int(input())
D = list(map(int, input().split()))

D.sort()
print(D[len(D) // 2] - D[len(D) // 2 - 1])
