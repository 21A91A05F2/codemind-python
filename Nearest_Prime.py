def isprime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True

t = int(input())
for _ in range(t):
    n = int(input())
    f,b = n,n
    while not isprime(f) and not isprime(b):
        f+=1
        b-=1
    if isprime(f) and isprime(b):
        print(min(f,b))
    elif isprime(f):
        print(f)
    else:
        print(b)
        