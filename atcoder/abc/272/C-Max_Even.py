N = input()
A = input().split()
A = list(map(int, A))
A.sort()

odd = []
even = []

for num in A:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

if len(odd) < 2:
    oddMax = -1
else:
    oddMax = odd[len(odd) - 1] + odd[len(odd) - 2]

if len(even) < 2:
    evenMax = -1
else:
    evenMax = even[len(even) - 1] + even[len(even) - 2]

if evenMax > oddMax:
    print(evenMax)
else:
    print(oddMax)
