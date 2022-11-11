N, A, B = map(int, input().split())
S = input()

sum = A + B
counter = 0
oversea = 1
for ele in S:
    if ele == "c":
        print("No")
    elif ele == "a":
        if counter < sum:
            print("Yes")
            counter += 1
        else:
            print("No")
    else:
        if counter < sum and oversea <= B:
            print("Yes")
            counter += 1
            oversea += 1
        else:
            print("No")
            oversea += 1
