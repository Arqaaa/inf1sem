A = list(map(int,input().split()))
B = []
x = len(A)




while len(A) != 0 :
    b = max(A)
    B.append(str(b))
    A.remove(b)
#if "".join(map(str, B)) == "0" * x :
#    print(0)
#else:
#   print("".join(map(str, B)))
B.sort(reverse=True)
print(B)



