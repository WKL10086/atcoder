s = input()

start = -1
end = -1
i = 0
while i < len(s):
    if start == -1:
        if s[i] == "A":
            start = i

    if s[i] == "Z":
        end = i

    i += 1

print(end - start + 1)
