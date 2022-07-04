n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=-1
for i in l:
    if i<a or i>b:
        if m<i:
            m=i
print(m)
