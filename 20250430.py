x = [2, 24, 65, 90, 34, 3, 94, 90, 2]
n = len(x)

print(range(n))
print(range(0, n))

for i in range(n):
    for j in range (i + 1, n):
        if x[i] == x[j]:
            print(f"数字{x[i]}は同じで")
            print(f"x[{i}]とx[{j}]は等しい")


