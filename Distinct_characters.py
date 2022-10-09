s=input()
s=s.lower()
k=list(set(s))
k.sort()
for i in k:
    if i==" ":
        del k[k.index(i)]
print("".join(k))