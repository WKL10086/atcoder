H, W = map(int, input().split())

layout = ["#" for _ in range(W + 2)]
print("".join(layout))

for i in range(H):
    pixel = input()
    print("#" + pixel + "#")

print("".join(layout))
