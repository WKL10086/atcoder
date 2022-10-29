A, B, C, D, E, F = map(int, input().split())

ans = (A * B * C) - (D * E * F)
ans %= 998244353

print(ans)
