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

while p != None:
    print(p.data)
    p = p.next