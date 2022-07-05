
n=int(input())
a=list(map(int,input().split()))
pro=1
for i in a:
    pro=1
    for j in range(0,n):
        if i!=a[j]:
            pro=pro*a[j]
    print(pro,end=' ')