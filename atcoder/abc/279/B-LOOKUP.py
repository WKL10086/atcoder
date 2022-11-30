S = input()
T = input()

ans = False

for i in range(len(S)):
    if S[i : i + len(T)] == T:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")
