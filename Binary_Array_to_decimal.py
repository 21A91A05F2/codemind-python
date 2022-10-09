n=int(input())
l=list(map(int,input().split()))
s=0
j=0
for i in range(n-1,-1,-1):
    if l[i]==1:
        #print(l[i])
        s+=2**j
    j+=1
print(s)