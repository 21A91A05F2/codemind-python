s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s=""
c=0
for i in s1:
    if i not in s2 and i not in s and i!=" ":
        s+=i
        c+=1
for i in s2:
    if i not in s1 and i not in s and i!=" ":
        s+=i
        c+=1
print(c)