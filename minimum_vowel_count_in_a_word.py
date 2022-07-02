
n=input()
v="aeiouAEIOU"
c=0
a=[]
for i in n:
    if i==' ':
        a.append(c)
        
        c=0
       
    elif i in v:
        c=c+1
a.append(c)
#print(a)
if len(a)!=0:
    print(min(a))
else:
    print('-1')