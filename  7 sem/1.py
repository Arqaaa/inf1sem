class Vector() :
    def __init__(self , x = 1 , y = 1 , z = 1):
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    def __add__(self, other):
        if isinstance(other , Vector):
            return Vector(self.x + other.x , self.y + other.y , self.z + other.z)
        elif isinstance(other , int) or isinstance(other , float):
            return Vector(self.x + other , self.y + other , self.z + other)
    def __radd__(self, other):
        return self + other
    def __matmul__(self, other):
        if isinstance(other , Vector):
            return Vector(self.x * other.x , self.y * other.y , self.z * other.z)
        elif isinstance(other , int) or isinstance(other , float):
            return Vector(self.x * other , self.y * other , self.z * other)
    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'

    def __inp__(self):
        A = list(map(int,input().split()))
        self.x = A[0]
        self.y = A[1]
        self.z = A[2]

if __name__  == "__main__" :

    n = int(input())
    v = []
    for i in range(n):
        a = Vector()
        a.__inp__()
        v.append(a)


    M = Vector(0 , 0 , 0)
    for i in range(len(v)) :
        M += v[i]

    C = M.__matmul__(1/len(v))

    print(C)
