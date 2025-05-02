n = 5
S = [None for _ in range(n)]

top = -1 #グローバル変数

def push(S,x):
    global top #変数topを関数ないで変更するためのグローバル宣言 
    top = top + 1
    if top == n:
        print("スタックアンダーフロー")
    else:
        S[top] = x

def pop(S):
    global top