n=int(input())
s=0
a=[]
for i in range(n):
    m=int(input())
    a.append(m)
t=int(input())
for k in a:
    if k<=t:
        s=s+1
    else:
        s=s+2
print(s)