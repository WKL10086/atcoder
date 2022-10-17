import re


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
        col[c] = [c]

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
        if cs in row:
            index = bs(row[cs], l, 0, len(row[cs]) - 1, d)
            if index != -1:
                cs = max(row[cs][index] + 1, cs - l)
            else:
                cs = max(1, cs - l)
        else:
            cs = max(1, cs - l)
    elif d == "R":
        if cs in row:
            index = bs(row[cs], l, 0, len(row[cs]) - 1, d)
            if index != len(row[cs]):
                cs = min(row[cs][index] - 1, cs + l)
            else:
                cs = min(W, cs + l)
        else:
            cs = min(W, cs + l)
    elif d == "U":
        if rs in col:
            index = bs(col[rs], l, 0, len(col[rs]) - 1, d)
            if index != -1:
                rs = max(col[rs][index] + 1, rs - l)
            else:
                rs = max(1, rs - l)
        else:
            rs = max(1, rs - l)
    elif d == "D":
        if rs in col:
            index = bs(col[rs], l, 0, len(col[rs]) - 1, d)
            if index != len(col[rs]):
                rs = min(col[rs][index] - 1, rs + l)
            else:
                rs = min(W, rs + l)
        else:
            rs = min(W, rs + l)

    print(str(rs) + " " + str(cs))
