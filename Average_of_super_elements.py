n=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    if i not in b and l.count(i)==i:
        b.append(i)
if len(b)==0:
    print(-1)
else:
    print("{:.2f}".format(sum(b)/len(b)))