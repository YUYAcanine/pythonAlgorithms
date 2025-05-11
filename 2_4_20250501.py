n = 5
S = [None for _ in range(n)]

top = -1 #グローバル変数

def push(S,x):
    global top #変数topを関数ないで変更するためのグローバル宣言 これで関数内で関数外で定義したものを使える
    top = top + 1
    if top == n:
        print("スタックアンダーフロー")
    else:
        S[top] = x

def pop(S):
    global top
    if top == -1:
        print("アンダーフロー")
    else:
        print("popで" + str(S[top]) + "を出力")
        S[top] = None
        top = top -1

push(S,1)
push(S,4)
push(S,2)
print(S)

pop(S)
pop(S)
print(S)