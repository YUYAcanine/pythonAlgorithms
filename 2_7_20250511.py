n = 5
Q = [None for _ in range(n)]

left = 0
right = 0

def enqueue(Q,x):
    global right
    Q[right] = x
    right = right + 1
    if right == n:
        right = 0
    if left == right:
        print("キューオーバーフロー")
    
def dequeue(Q):
    global left
    if left == right:
        print("アンダーフロー")
    else:
        print("deqeueで" + str(Q[left]) + "を出力")
        Q[left] = None
        left = left + 1
    if left == n:
        left = 0

enqueue(Q,1)
enqueue(Q,4)
enqueue(Q,2)
print(Q)

enqueue(Q,3)
dequeue(Q)
dequeue(Q)
print(Q)

