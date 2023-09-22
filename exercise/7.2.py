A = list(map(int,input().split()))
s = A[0]
for i in range(0 , len(A)):
    if A.count(A[i]) > A.count(s) :
        s = A[i]
print(s)