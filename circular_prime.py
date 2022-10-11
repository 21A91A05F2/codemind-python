def prime(n):
    while n>0:
        c=0
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                c+=1
        if c==0:
            return n
        return False
n=int(input())
if prime(n):
    k=0
    while(n>0):
        r=n%10
        k=k*10+r
        n=n//10
else:
    print("not prime")
if prime(k):
    print("circular prime")
else:
    print("prime but not a circular prime")
    
        
    