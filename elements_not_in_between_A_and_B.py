n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=[]
c=0
for i in l:
    if i<a or i>b:
        m.append(i)
        c+=1
if(c>0):
    print(*m)
else:
    print(-1)



