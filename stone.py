from random import randrange
A = [randrange(-10, 10) for i in range(10)]
print(A)

def bubble_method(A):
    length = len(A)
    for i in range(length-1, 0, -1):
        for j in range(length-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

print(bubble_method(A))
