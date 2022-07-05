n,m=map(int,input().split())
l=[];ma=0
for i in range(0,n):
    a=list(map(int,input().split()))
    l.append(a)
for j in range(0,m):
    ma=l[0][j]
    for i in range(0,n):
        if l[i][j]>ma:
            ma=l[i][j]
    print(ma)