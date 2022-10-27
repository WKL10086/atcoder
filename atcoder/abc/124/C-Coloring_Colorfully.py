S = input()

string_1 = ""
string_2 = ""

for i in range(len(S)):
    if i % 2 == 0:
        string_1 += "0"
        string_2 += "1"
    else:
        string_1 += "1"
        string_2 += "0"

diff_1 = 0
diff_2 = 0

for i in range(len(S)):
    if S[i] != string_1[i]:
        diff_1 += 1

    if S[i] != string_2[i]:
        diff_2 += 1

ans = min(diff_1, diff_2)
print(ans)
