n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=[]
for i in l:
    if l.count(i)==k and i not in a:
        a.append(i)
if len(a)==0:
    print(-1)
else:
    print(*a)