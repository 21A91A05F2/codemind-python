n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    c=0
    if i==0:
        c=1
        b.append(c)
        continue
    if i<0:
        i=i*(-1)
    while i:
        d=i%10
        c+=1
        i//=10
    b.append(c)
for i in range(n):
    if b[i]==max(b):
        print(a[i],end=' ')