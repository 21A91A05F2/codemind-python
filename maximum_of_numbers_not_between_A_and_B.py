n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
mx=0
for i in range(n):
    if (l[i]<a or l[i]>b) and l[i]>mx:
        mx=l[i]
if mx==0:
    print(-1)
else:
    print(mx)