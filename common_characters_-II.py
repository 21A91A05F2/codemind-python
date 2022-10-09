s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
c=0
s=""
for i in s1:
    if i in s2 and i not in s and i!=" ":
        s+=i
        c+=1
print(c)