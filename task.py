from random import *
A = [randint(-10,10) for i in range(10)]
print(A)

def bubble(A , show = False):
    iteration = 0
    if show:
        print('iteration' , iteration , ';' , *A)
    n = len(A)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]
        if show:
            iteration +=1
            print('iteration', iteration, ';', *A)
    return A
print(bubble(A, True))
