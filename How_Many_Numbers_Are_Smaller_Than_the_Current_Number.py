n=int(input())
a=list(map(int,input().split()))
s=len(a)
c=0
for i in range(0,s):
    c=0
    for j in range(0,s):
        if a[j]<a[i] and j!=i:
            c+=1
    print(c,end=' ')        