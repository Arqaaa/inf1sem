a=int(input())
b=int(input())

def aaa(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

while a != 0 and b != 0 :
    if a > b :
        a = a % b
    else :
        b = b % a
    d = a + b
x = 0
y = 0
q = x*a + y*b
while q != d :
        while True :
            x += -1
            y = (d-a*x)/b
            if aaa(y) == True:
                break
print(x,y)


