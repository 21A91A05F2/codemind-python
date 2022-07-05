
n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if a[j]!=-1:
            if a[i]==a[j] and i!=j:
                print(a[i])
                a[j]=-1
        