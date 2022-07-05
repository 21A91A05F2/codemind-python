n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if a.count(i)>a.count(c):
        c=i
    if a.count(i)==a.count(c):
        c=min(i,c)
print(c)
