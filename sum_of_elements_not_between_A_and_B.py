n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=0
for i in l:
    if i<a or i>b:
        m=m+i
print(m)
