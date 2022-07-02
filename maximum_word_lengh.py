n=input()
x=n.split()
l=[]
for i in x:
    p=str(i)
    q=len(p)
    l.append(q)
print(max(l))