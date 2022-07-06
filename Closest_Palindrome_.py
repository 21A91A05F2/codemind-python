n=int(input())
l=[]
for i in range(n//2,n):
    temp=i
    rev=0
    while(i):
        d=i%10
        rev=rev*10+d
        i=i//10
    if(temp==rev):
        l.append(rev)
        l.reverse()
for i in l:
    temp=i
    break
m=n-temp
for i in range(n+1,n**2):
    tem=i
    rev=0
    while(i):
        d=i%10
        rev=rev*10+d
        i=i//10
    if(tem==rev):
        k=abs(n-rev)
        break
if(m==k):
    print(temp,rev)
elif(m>k):
    print(rev)
else:
    print(temp)
