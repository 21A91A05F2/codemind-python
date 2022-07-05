n=int(input())
a=list(map(int,input().split()))
c=0
v=0
for i in a:
    if i==1:
        c+=1
        v=max(v,c)
    else:
        c=0
print(v)