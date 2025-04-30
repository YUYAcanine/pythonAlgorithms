class Clac:
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c
    
    def plus(self):
        return self.x + self.y + self.z
    
    def times(self):
        return self.x * self.y * self.z
    
data1 = Clac(10, 20, 60)
data2 = Clac(20, 100, 1000)

print(data1.x, data1.y, data1.z)
print(data1.plus())
print(data2.plus())
print(data1.times())
print(data2.times())
    