N = int(input())
A = str(input())
s=""
j=0
p=N
w=A[0:N]
w=w[::-1]
for i in range(int(len(A)/N)) :
    print("indices are from", p-1, 'to', j-1)
    print("string is", A[p-1:j-1:-1])
    s += A[p-1:j-1:-1]
    p =p+N
    j +=N
print(w+s)
