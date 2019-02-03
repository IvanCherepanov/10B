#2.1
from random import randrange as rnd
A=[rnd(10) for i in range(10)]
print(A)
k=int(len(A)/2)
k1=A[k:]
k2=A[:k]
k3=k1+k2
print(k3)
#2.2
A[1],A[2]=A[2],A[1]
A[3],A[4]=A[4],A[3]
A[5],A[6]=A[6],A[5]
A[7],A[8]=A[8],A[7]
print(A)
#2.3
A[0],A[9]=A[9],A[0]
A[1],A[8]=A[8],A[1]
A[2],A[7]=A[7],A[2]
A[3],A[6]=A[6],A[3]
A[4],A[5]=A[5],A[4]
print(A)
