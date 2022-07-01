string=input()
c=0
a=[]
vowels='aeiouAEIOU'
for s in string:
    if s in vowels:
        if s not in a:
            a.append(s)
if len(a)!=0:
   
    print(*a)
else:
    print('-1')