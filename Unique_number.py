n=int(input())
l=[]
while(n):
    m=n%10
    l.append(m)
    n=n//10
c=0
k=len(l)
for i in l:
    if l.count(i)==1:
        c+=1
    else:
        print("Not Unique Number")
        break
if(c==k):
    print("Unique Number")
