def isprime(n):
    if n<2:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
n=int(input())
l=list(map(int,input().split()))
c=0
d,f=l.index(min(l)),l.index(max(l))
if d<f:
    for i in range(d,f+1):
        if isprime(l[i]):
            c+=1
else:
    for i in range(f,d+1):
        if isprime(l[i]):
            c+=1
print(c)