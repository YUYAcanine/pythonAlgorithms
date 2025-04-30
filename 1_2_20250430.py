n = int(input("n = "))
B = [0]*n
S = 0

#自分の回答
for i in range(0,n):
    B[i] = int(input(f"B[{i}] = "))
    m = len(B) - i - 1
    S += B[i]*2**m
print(S)

#模範解答
d = B[0]
for i in range(1,n):
    d = d*2 + B[i]
    print(d)
print(d)