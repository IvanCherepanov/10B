from random import*
a=[randint(-10,10) for i in range (10)]
print(a)
def bubble(a):
         for i in range(n-1):
                  for j in range(n-1,i,-1):
                           if a[j]<a[j-1]:
                                    a[j],a[j-1]=a[j-1],a[j]
         print(bubble(a))                           
