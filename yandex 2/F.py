n, m = map(int, input().split())
while m != 0 or n != 0:
    q = input()
    A = [int(i) for i in str(q)]
    z = len(A)

    i = 0
    k = 0

    while k != m and i != len(A) - 1:
        while A[i] < A[i + 1] and i > -1 and k != m :
            A.pop(i)
            i -= 1
            k += 1
        i += 1

    A = A[0:n -m]


    print(int(''.join(map(str, A))))

    n, m = map(int, input().split())
