N =int(input())
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

k = 0
M = len(X)
s = sum(X)/M


for i in range(M) :
    if abs(s - X[i]) ==  abs(X[M-i - 1] - s)  and Y[i] == Y[M - i - 1] or X[i] == s :
        k += 1
print(k)

if k == M :
    print('Yes')
else:
    print('No')