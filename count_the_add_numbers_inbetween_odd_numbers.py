n=int(input())
a=list(map(int,input().split()))
#print(a)
c=0
for i in range(0,n-2,1):
    if a[i]%2!=0  and a[i+1]%2 and a[i+2]%2!=0:
        c+=1
print(c)