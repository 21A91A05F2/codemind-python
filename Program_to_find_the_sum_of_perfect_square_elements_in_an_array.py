n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    m=i**0.5
    if(m==int(m)):
        if(i==m*m):
            s=s+i
print(s)