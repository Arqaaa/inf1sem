n = int(input())
A = list(map(int, input().split()))
S = 0

while len(A) != 0 :
    max_tmp = max(A)
    k = A.index(max_tmp)
    for i in range(k):
        S += max_tmp - A[i]
    A = A[k+1: ]

print(S)
