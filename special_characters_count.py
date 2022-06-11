n=input()
c=0
for i in n:
    if i.isalpha() or i.isdigit() or i==" ":
        continue
    else:
        c+=1
print(c)