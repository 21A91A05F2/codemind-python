n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(0,n):
    if l[i]%2:
        s=s+l[i]
print(s)