def isprime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
n1=int(input())
n2=int(input())
s=n1+n2
k=s+1
while not isprime(k):
    k+=1
print(k-s)