m , n = input().split()
m = int(m)
n = int(n)
k = 0
l = 0
L = 0
K = 0


while True :
    M = ((m-1)/(2**k)) % 3
    N = ((n-1)/(2**l)) % 3
    k += 1
    l +=1

    if (M == 0 and N != 0) or (N != 0 and M == 0) or (N != 0 and M != 0):
        break

while True :
    M = ((m - 1) / (2 ** k)) % 3


for i in range(k) :
    K += 2**(i+1)

for j in range(l) :
    L += 2**(j+1)

print(K+L)
