n=int(input())
l=list(map(int,input().split()))
s=0
k=0
for i in l:
    if i%2==0:
        s=s+1
    else:
        k=k+1
print(s,k)