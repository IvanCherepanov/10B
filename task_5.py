#5.1
from random import randrange as rnd
A=[rnd(20) for i in range(20)]
print(A)
A.insert(4,100)
print(A)
#5.2
n=int(input('Введите число -> '))
m=int(input('Введите номер элемента(меньше 20)->'))
A.insert(m,n)
print(A)
