from random import randrange as rnd
A=[rnd(-10,10) for i in range (10)]
print(A)

def bubble(A):
    n=len(A)
    for i in range (n-1):
        for j in range(n-1,i,-1):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
    return A
print(bubble(A))
