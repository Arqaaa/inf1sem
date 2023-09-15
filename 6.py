f = open(r"C:\aaa.txt")
A = list(map(int,f.readline().split()))
s=list(map(str,f.readline().split()))
b=f.readline()
b=int(b)
k=1
x=0
l=0
o=0
y=1
w=0
for i in range(len(A)):
    while A[i]>0 :
        k=A[i]%10
        x+=k*(b**l)
        l+=1
        A[i]=A[i]//10
    A[i] = x
    l=0
    k =0
    x=0
print(A)
if s[0] == '+' :
    y=0
    for i in range(len(A)) :
        y += A[i]
elif s[0] =="-" :
    y=0
    for i in range(len(A)):
        y -=A[i]
else :
    for i in range(len(A)):
        y *= A[i]
print(y)
while y > 0 :
    p = y % b
    o += p * (10 ** w)
    w += 1
    y=y//b
print(o)
f = open(r"C:\bbb.txt", 'w')
o=str(o)
f.write(o)
