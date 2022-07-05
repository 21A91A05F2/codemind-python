
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
c=n
s=0
t=0
for i in range(n):
    for j in range(c):
        if i==j:
            s=s+a[i][i]
for i in range(n):
    t=t+a[i][n-i-1]
print('Principal Diagonal:'+str(s))
print('Secondary Diagonal:'+str(t))