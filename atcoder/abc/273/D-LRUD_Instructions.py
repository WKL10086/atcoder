def bs(array, x, low, high, type):
    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    if type == "L" or type == "U":
        return high
    elif type == "R" or type == "D":
        return low


H, W, rs, cs = map(int, input().split())
N = int(input())
row = {}
col = {}


i = 0
while i < N:
    r, c = map(int, input().split())

    if r in row:
        row[r].append(c)
    else:
        row[r] = [c]

    if c in col:
        col[c].append(r)
    else:
        col[c] = [r]

    i += 1

for x in row:
    row[x].sort()

for x in col:
    col[x].sort()

Q = int(input())
i = 0
while i < Q:
    d, l = input().split()
    l = int(l)

    if d == "L":
        if rs in row:
            index = bs(row[rs], cs, 0, len(row[rs]) - 1, d)
            if index != -1:
                cs = max(row[rs][index] + 1, cs - l)
            else:
                cs = max(1, cs - l)
        else:
            cs = max(1, cs - l)
    elif d == "R":
        if rs in row:
            index = bs(row[rs], cs, 0, len(row[rs]) - 1, d)
            if index != len(row[rs]):
                cs = min(row[rs][index] - 1, cs + l)
            else:
                cs = min(W, cs + l)
        else:
            cs = min(W, cs + l)
    elif d == "U":
        if cs in col:
            index = bs(col[cs], rs, 0, len(col[cs]) - 1, d)
            if index != -1:
                rs = max(col[cs][index] + 1, rs - l)
            else:
                rs = max(1, rs - l)
        else:
            rs = max(1, rs - l)
    elif d == "D":
        if cs in col:
            index = bs(col[cs], rs, 0, len(col[cs]) - 1, d)
            if index != len(col[cs]):
                rs = min(col[cs][index] - 1, rs + l)
            else:
                rs = min(H, rs + l)
        else:
            rs = min(H, rs + l)

    print(str(rs) + " " + str(cs))
    i += 1
