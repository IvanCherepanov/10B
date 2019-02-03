#4.1
from random import randrange as rnd
A=[rnd(10) for i in range(10)]
print(A)
del A[4]
print(A)
#4.2
k=int(input('Введите номер элемента -> '))
del A[k-1]
print(A)



