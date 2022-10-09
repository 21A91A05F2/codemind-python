n = int(input())
l = list(map(int,input().split()))
a=[]
for i in range(0,n,2):
    for j in range(0,l[i+1]):
        a.append(l[i])
print(*a)