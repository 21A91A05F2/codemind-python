

s=input()
l=s.split(" ")
v="aeiouAEIOU"
for i in l:
    c=0
    for j in i:
        if j in v:
            c+=1
    print(c,end=" ")