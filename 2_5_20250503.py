a = 1

def plus(b):
    global a
    a = 2
    c = a + b
    print("local a =",a)
    return c

b = int(input("b = "))

print("golobal a =", a)
print(a, "+", b, "=", plus(b))