k=int(input())
m=list(map(int,input().split()))
n=[]
for i in range(0,k,2):
    for j in range(0,m[i+1]):
        n.append(m[i])
print(*n)