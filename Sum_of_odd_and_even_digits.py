n=int(input())
l=list(map(int,input().split()))
c=0
k=0
for i in range(0,n):
    if i%2==0:
        c=c+l[i]
    else:
        k=k+l[i]
d=c-k
if d==0:
    print("YES")
else:
    print("NO")