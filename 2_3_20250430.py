class Record:
    def __init__(self, data, next):
        self.data = data
        self.next = next
R1 = Record(9, None)
print(R1.data)
print(R1.next)

R2 = Record(2, R1)
R3 = Record(0, R2)
R4 = Record(4, R3)
head = Record(5,R4)

p = head
print("初期リスト")
while p != None:
    print(p.data)
    p = p.next

head = Record(3, head) #headの前に3を追加
print("3を追加した後")
p = head
while p != None:
    print(p.data)
    p = p.next

if head is None:
    print("消去するデータはない")
else:
    print("先頭のデータは"+ str(head.data))
    head = head.next #head.dataの3を飛ばしてしまう

p = head
print("先頭消去後")
while p != None:
    print(p.data)
    p = p.next
