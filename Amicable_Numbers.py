n=int(input())
m=int(input())
c=0
k=0
for i in range(1,n):
    if n%i==0:
        c=c+i
for j in range(1,m):
    if m%j==0:
        k=k+j
if c==m and k==n:
    print('Amicable')
else:
    print('Not Amicable')
