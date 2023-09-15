S = str(input())
d=""
k=0
p =""
for i in range(len(S)) :
    d = S[k:k+2]
    d = d[::-1]
    p += d
    k += 2
print(p)