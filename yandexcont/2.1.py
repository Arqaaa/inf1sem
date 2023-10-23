a = int(input())
b = int(input())
k = -1

while True :
    k += 1
    x = b*k - a

    if  ( (a + x) % b) == 0  and ( (b + x) % a) == 0:
        break

print(k)