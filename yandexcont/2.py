a , b = in
a = int(a)
b = int(b)
x = -1

while True :
    x += 1
    A = (a + x) / b
    B = (b + x) / a
    if A == int(A) and B == int(B) :
        break

print(x)