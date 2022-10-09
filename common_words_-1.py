s1=input()
s2=input()
l1=list(s1.lower().split(" "))
l2=list(s2.lower().split(" "))
c=0
for i in l1:
    if i in l2 :
        c+=1
print(c)