N = int(input())
S = list(map(int, input().split()))
ans = []

prev = 0
for ele in S:
    ans.append(ele - prev)
    prev = ele

print(" ".join(map(str, ans)))
