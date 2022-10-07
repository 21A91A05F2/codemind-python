def isprime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return n

n = int(input())
f,b = n,n
while not isprime(f) and  not isprime(b):
    f+=1
    b-=1
if isprime(f) and isprime(b):
    fn,bn = abs(n-f),abs(n-b)
    print(min(fn,bn))
else:
    fn = abs(n-f)
    bn = abs(n-b)
    print(min(fn,bn))