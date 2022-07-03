from math import sqrt
def prime(i):
    if i==1:
        return 0
    for j in range(2,int(sqrt(i))+1):
        if i%j==0:
            return 0
    return 1
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if prime(i)==1:
        c+=1
print(c)