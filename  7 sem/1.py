class Vector() :
    def __init__(self , x = 0 , y = 0 , z = 0):
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
    def __sec__(self , other):
        return 0.5 * (Vector(self.y * other.z - self.z * other.y , self.z * other.x - self.x * other.z , self.x * other.y - self.y * other.x).__abs__())




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
    print(v[0].__sec__(v[1]))
    L = []
    l = []
    S = []

    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            for k in range(j + 1 , len(v)):
                a = Vector()
                b = Vector()
                a += v[i] + v[j].__matmul__(-1)
                b += v[i] + v[k].__matmul__(-1)
                s = a.__sec__(b)
                S.append(s)

    print(max(S))



