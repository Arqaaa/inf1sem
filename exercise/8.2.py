A = []
n =int(input())
m = 0
t = 0
for i in range(n):
    A.append(int(input()))
for i in range(len(A)):
    m = 0
    t = 0
    for o in range(0 , len(A)) :
        if A[i] >= A[o] :
            m += 1
        if A[i] <= A[o] :
            t += 1
    if m >=((n+1)/2) and t >= ((n+1)/2):
        w = A[i]
print(w)