n=int(input())
p=0
while(n):
    r=n%10
    n=n//10
    if(p<r):
        p=r
print('%d'%p)
