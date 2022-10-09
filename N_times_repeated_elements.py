n=int(input())
a=list(map(int,input().split()))
c=int(input())
b=[]
for i in a:
    if i not in b and a.count(i)==c:
        b.append(i)
if len(b)==0:
    print(-1)
else:
    print(*b)
    