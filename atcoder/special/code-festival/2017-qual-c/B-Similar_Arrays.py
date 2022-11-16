N = int(input())
A = list(map(int, input().split()))


counter = 0
for ele in A:
    if ele % 2 == 0:
        counter += 1

ans = 3**N - 2**counter

print(ans)
