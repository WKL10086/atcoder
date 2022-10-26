A, B = map(int, input().split())
S = input().split("-")

if len(S) == 2 and len(S[0]) == A and len(S[1]) == B:
    print("Yes")
else:
    print("No")
