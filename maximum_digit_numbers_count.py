n=int(input())
l=list(map(int,input().split()))
m=int(len(str(max(l))))
a=[]
for i in l:
    c=0
    if i==0:
        c=1
        a.append(c)
        continue
    if i<0:
        i=i*(-1)
    if i>0:
        k=len(str(i))
        a.append(k)
for i in range(n):
    if a[i]==max(a):
        print(l[i],end=" ")
