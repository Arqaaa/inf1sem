a =[1,2,3,4,5,6,6,6,6]
b = [4,5,6,7,8,8,8]

A = set(a)
B = set(b)
print(A)
print(B)


print(A.union(B)-A.intersection(B))
print(A.intersection(B))