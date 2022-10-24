N, M, X = map(int, input().split())
A = list(map(int, input().split()))

# can use binarySearch(A), then min(min,right)
left = [x for x in A if x < X]
right = [x for x in A if x > X]

ans = min(len(left), len(right))

print(ans)
