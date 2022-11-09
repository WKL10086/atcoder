N, M = map(int, input().split())

problems = [0 for _ in range(N)]
correct_idx = set()

for _ in range(M):
    P, S = input().split()
    P = int(P)

    if S == "WA":
        if P not in correct_idx:
            problems[P - 1] += 1
    else:
        correct_idx.add(P)

wrongCounter = 0
for ele in correct_idx:
    wrongCounter += problems[ele - 1]

print(str(len(correct_idx)) + " " + str(wrongCounter))
