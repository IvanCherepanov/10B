def bubble(A):
    N = len(A)
    for i in range(N-1):
        for j in range(N-1,i,-1):
            if A[j]<A[j-1]:
                A[j],A[j-1] = A[j-1], A[j]
    return A



from random import randrange as rnd
A = [rnd(-10,10) for i in range(10)]

print(bubble(A))

