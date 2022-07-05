n=int(input())
a=list(map(int,input().split()))
b=int(input())
k=max(a)
for i in range(n):
    if a[i]+b<k:
        print("False",end=' ')
    else:
        print("True",end=' ')