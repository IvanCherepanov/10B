from random import *
s=[randint(-10,10) for i in range (10)]
n=len(s)
for i in range(n-1):
    for j in range(n-1,i,-1):
        if s[j]<s[j-1]:
            s[j],s[j-1]=s[j-1],s[j]
print(s)
