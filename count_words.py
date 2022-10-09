s=input()
a=list(s.split(" "))
c=0
for i in a:
    if i[0] in "aeiouAEIOU" and i[-1] not in "aeiouAEIOU":
        c+=1
print(c)