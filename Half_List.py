n=int(input())
a=list(map(int,input().split()))
s=len(a)
for i in range(s-1,s//2-1,-1):
    print(a[i],end=' ')
for i in range(0,s//2,1):
    print(a[i],end=' ')