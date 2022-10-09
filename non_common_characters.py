s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
k=list(set(s1))
l=list(set(s2))
m=[]
for i in k:
    if i not in l and i not in m and i!=" ":
        m.append(i)
for i in l:
    if i not in k and i not in m and i!=" ":
        m.append(i)
m.sort()
print("".join(m))