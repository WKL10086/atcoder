N = int(input())

words = ["" for _ in range(N)]
ans = "Yes"

for i in range(N):
    W = input()

    if i != 0:
        prevWord = words[i - 1]

        if W not in words and W[0] == prevWord[-1]:
            words[i] = W
        else:
            ans = "No"
            break
    else:
        words[i] = W

print(ans)
