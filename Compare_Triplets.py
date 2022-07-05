
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0;v=0
if a[0]>b[0]:
     c+=1
if a[1]>b[1]:
    c+=1
if a[2]>b[2]:
    c+=1
if a[0]<b[0]:
    v+=1
if a[1]<b[1]:
    v+=1
if a[2]<b[2]:
    v+=1
print(c,v);