s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
a=list(s1.split(" "))
b=list(s2.split(" "))
c=[]
for i in b:
    if i in a and i not in c:
        c.append(i)
print(" ".join(c))