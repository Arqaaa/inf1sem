a = list(map(int, input().split()))
a = [0] + a
n = len(a)

b = [0] * n
b[1] = max(a[0],a[1])
b[0] = a [0]
for i in range(2, n):
    b[i] = max(b[i-1], b[i-2] + a[i])

print(b[-1])