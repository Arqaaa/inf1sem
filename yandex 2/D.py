A = input()

b = ['[' , '(' , '{']
c = [']' , ')' , '}']
B = []

q = 1
for i in range(len(A)) :
    if A[i] in b:
        B.append(A[i])
    else:
        if A[i] == ')' :
            if B[-1] == '(':
                B.pop(-1)
            else:
                q = 0
        if A[i] == ']':
            if B[-1] == '[':
                B.pop(-1)
            else:
                q = 0
        if A[i] == '}':
            if B[-1] == '{':
                B.pop(-1)
            else:
                q = 0

if len(B)>0:
    q = 0

if q == 1 :
    print("Yes")
else:
    print("No")