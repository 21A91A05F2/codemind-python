n,x=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    if i>=x:
        b.append(a[i])
for i in range(n):
    if i<x:
        b.append(a[i])
print(*b)