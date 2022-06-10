n=int(input())
m=int(input())
s=0
for i in range(0,n):
    a=list(map(int,input().split()))
    s=s+sum(a)
print(s)