n=int(input())
a=list(map(int,input().split()))
maxi=a[n-1]
a[n-1]=-1
for i in range(n-2,-1,-1):
    temp=a[i]
    a[i]=maxi
    if maxi<temp:
        maxi=temp
for i in a:
    print(i,end=' ')