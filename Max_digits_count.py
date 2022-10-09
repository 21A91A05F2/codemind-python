n=int(input())
a=list(map(int,input().split()))
m=max(a)
c=0
for i in a:
    if len(str(m))==len(str(i)):
        c+=1
print(c)