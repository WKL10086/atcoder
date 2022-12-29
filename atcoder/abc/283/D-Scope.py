S = input()

stack = ""
complete = True
remember = []

for ele in S:
    if ele == "(":
        remember.append(stack)
    elif ele == ")":
        stack = remember.pop()
    else:
        if ele not in stack:
            stack += ele
        else:
            complete = False
            break

print("Yes" if complete else "No")
