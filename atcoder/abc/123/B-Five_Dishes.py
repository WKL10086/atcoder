import math


dish = [0 for _ in range(5)]

i = 0
while i < 5:
    dish[i] = int(input())
    i += 1


def sortFunc(ele):
    x = str(ele)
    if x[len(x) - 1] == "0":
        return 9.9
    else:
        return int(x[len(x) - 1])


dish.sort(key=sortFunc, reverse=True)

ans = 0
i = 0
while i < 4:
    ans += math.ceil(dish[i] / 10) * 10
    i += 1

ans += dish[4]

print(ans)
