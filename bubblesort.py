from random import *
A=[randint(-10,10)for i in range(10)]
print (A)

def bubbls(A):
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if A[j] < A[j,-1]:
                A[j],A[j-1]=A[j-1],A[j]
    return A
print(bubble(A))
