N = int(input())
T, A = map(int, input().split())

H = list(map(int, input().split()))
H = map(lambda x: T - (x * 0.006), H)

idx = [i for i in range(1, N + 1)]
palaces = dict(zip(idx, H))

ans = dict(sorted(palaces.items(), key=lambda x: abs(x[1] - A)))

print(next(iter(ans)))
