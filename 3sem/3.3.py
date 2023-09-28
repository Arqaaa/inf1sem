a=int(input())
b=int(input())
e =a
w=b
while a != 0 and b != 0 :
    if a > b :
        a = a % b
    else :
        b = b % a
    d = a + b

x = 0
y = 0
x1=0
y1=0
q = x*e + y*w
q1 = x*e + y*w

while q != d :
        while True :
            x += -1
            y = (d-e*x)/w
            q = x * e + y * w
            if int(y) == y:
                break

while q1 != d :
        while True :
            x1 += 1
            y1 = (d-e*x1)/w
            q1 = x1 * e + y1 * w
            if int(y1) == y1:
                break

if abs(x) + abs(y) < abs(x1) + abs(y1) :
    print(x,int(y))
else :
    print(x1, int(y1))
