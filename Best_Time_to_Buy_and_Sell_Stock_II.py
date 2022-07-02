n=int(input())
a=list(map(int,input().split()))
r=0
for i in range(1,n):
    if a[i]-a[i-1]>0:
        r=r+a[i]-a[i-1]
print(r)