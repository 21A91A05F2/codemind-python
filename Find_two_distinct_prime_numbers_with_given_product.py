def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
for i in range(2,(n//2)+1):
    for j in range(2,(n//2)+1):
        if isprime(i) and isprime(j) and i*j==n:
            print(i,j)
            exit()
print(-1)