n=int(input())
a=list(map(int,input().split()))
s=int(input())
res=-1
for i in range(n):
    if a[i]==s:
        res=i
print(res)