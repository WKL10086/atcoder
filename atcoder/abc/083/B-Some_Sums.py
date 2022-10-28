N, A, B = map(int, input().split())

ans = 0

i = 1
while i < N + 1:

    counter = 0
    for ele in str(i):
        counter += int(ele)

    if counter >= A and counter <= B:
        ans += i

    i += 1


print(ans)
