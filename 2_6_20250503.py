a = 1

def plus(b):
    global a  # これにより「関数内でもグローバルaを使う」
    a = 2     # グローバルaを書き換える
    c = a + b
    print("local a =", a)
    return c

b = 3
print("global a =", a)  # 1
print(plus(b))  # 1 + 3 = 5（実際は2 + 3）
print("after function, global a =", a)  # **2** に変わっている！