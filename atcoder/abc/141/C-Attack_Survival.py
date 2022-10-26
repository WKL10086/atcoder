N, K, Q = map(int, input().split())
score = [0 for _ in range(N)]

i = 0
while i < Q:
    A = int(input())
    score[A - 1] += 1

    i += 1

for ele in score:
    if Q - ele >= K:
        print("No")
    else:
        print("Yes")
