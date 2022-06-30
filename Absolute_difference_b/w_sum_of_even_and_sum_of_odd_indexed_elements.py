n=int(input())
l=list(map(int,input().split()))
s=0
k=0
for i in range(0,n):
    if i%2==0:
        s=s+l[i]
    else:
        k=k+l[i]
print(abs(s-k))