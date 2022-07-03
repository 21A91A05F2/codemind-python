n=int(input())
a=list(map(int,input().split()))
for i in a:
    c=0
    if i!=0:
        for j in a:
            if i==j:
                c+=1
    if i!=0:
        print(i,c,end=' ')
    for j in range(n):
        if i==a[j]:
            a[j]=0