n = int(input("要素の個数 = "))
x = [0]*n

for m in range(n):
    x[m] = int(input(f"x[{m}] = ")) #i,j,k,l,m,n

for i in range(n):
    for j in range(i+1,n):
        for k in range(n):
            if i != k and j != k and x[i]+x[j]==x[k]:
                print(x[i], x[j], x[k])

