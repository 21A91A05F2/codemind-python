n=int(input())
a=list(map(int,input().split()))
v=0
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[i]==a[j] and i!=j:
            c+=1
    if(c==0):
        if(v<a[i]):
            v=a[i]
if(v==0):
    print(-1)
else:
    print(v)