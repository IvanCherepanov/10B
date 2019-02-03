#3
from random import randrange as rnd
A=[rnd(10) for i in range(15)]
print(A)

A = [int(i) for i in A]
for i in range(len(A)//2):
    b = A[i]
    A[i] = A[len(A)-i-1]
    A[len(A)-i-1]=b
print(A)
