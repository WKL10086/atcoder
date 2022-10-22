N = int(input())
V = list(map(int, input().split()))

V.sort()

ans = V[0] / (2 ** (len(V) - 1))

i = 1
while i < len(V):
    ans += V[i] / (2 ** (len(V) - i))
    i += 1

print(ans)
