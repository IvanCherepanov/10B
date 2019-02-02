print('#2.1')
from random import randrange as rnd
n=int(input('Введите чётное число элементов -> '))
if n%2>0:
    print('Введено неверное количество элементов. Повторите попытку')
else:
    A=[rnd(-10,10) for i in range(n)]
    print(A)
    A[n//2], A[n//2-1] = A[n//2-1], A[n//2]
    print(A)


print('#2.2')
from random import randrange as rnd
C=[rnd(-10,10) for i in range(6)]
print(C)
C[0],C[1]=C[1],C[0]
C[2],C[3]=C[3],C[2]
C[4],C[5]=C[5],C[4]
print(C)

print('#2.3')
from random import randrange as rnd
k=int((input('Введите чётное число элементов -> ')))
if n%2>0:
    print('Введено неверное количество элементов. Повторите попытку')
else:
    B=[rnd(-10,10) for i in range(k)]
    print(B)
    B[k//2-1],B[k-1]=B[k-1],B[k//2-1]
    B[k//2],B[0]=B[0],B[k//2]
print(B)
