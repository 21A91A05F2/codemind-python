n=int(input())
a=list(map(int,input().split()))
c=0
v=0
for i in range (0,n):
    c=1
    for j in range(i+1,n):
        if a[i]==a[j]:
            c+=1
    
    if c%2==0:
        v+=1
        
print(v)