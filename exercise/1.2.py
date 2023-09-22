n=int(input())
A=[]
for i in range(n-1) :
    A.append(int(input()))
print(A)
for i in range(len(A)) :
    if A[i]!=i+1 :
        k = i+1
        break
print(k)
