N = int(input())

words = {}
counter = 0

for i in range(N):
    S = input()

    if S not in words:
        words[S] = 1
        counter = max(counter, 1)
    else:
        words[S] += 1
        counter = max(counter, words[S])

words = dict(sorted(words.items()))

for key in words:
    if words[key] == counter:
        print(key)
