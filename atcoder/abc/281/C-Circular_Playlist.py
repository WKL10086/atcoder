N, T = map(int, input().split())
A = list(map(int, input().split()))

total_time = sum(A)
remain_time = T % total_time

for i, ele in enumerate(A):
    if remain_time - ele < 0:
        print(i + 1, end=" ")
        print(remain_time)
        break
    else:
        remain_time -= ele
