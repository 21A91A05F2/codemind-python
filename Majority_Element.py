
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    s=0
    for j in range(n):
        if l[i]==l[j]:
            s+=1
    if s>n//2:
        print(l[i])
        break     