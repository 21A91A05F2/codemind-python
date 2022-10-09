
s=input()
s=s.lower()
k=set(s)
g=[]
for i in k:
    if i!=" ":
        g.append(i)
print(len(g))