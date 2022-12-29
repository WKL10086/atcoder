N, M = map(int, input().split())

participants = []
for _ in range(N):
    participant = input()
    participants.append(participant)

ans = 0
for i, target in enumerate(participants):
    for other in participants[i + 1 :]:
        correct = True
        for match in range(M):
            if not (target[match] == "o" or other[match] == "o"):
                correct = False
                break
        if correct:
            ans += 1

print(ans)
