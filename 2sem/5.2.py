A = list(map(int,input().split()))
for i in range(len(A) - 2, -1, -1):
    A[i] , A[i+1] = A[i+1] , A[i]
print(A)
