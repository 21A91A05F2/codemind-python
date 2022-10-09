s1=input()
s2=input()
l1=list(s1.lower().split(" "))
l2=list(s2.lower().split(" "))
c=0
for i in l1:
    if i in l2 and l1.count(i)==1 and l2.count(i)==1:
        c+=1
print(c)