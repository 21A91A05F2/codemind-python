s=input()
c=0
for i in range(0,len(s)):
    if s[i].isdigit():
        c+=1
if c>=1:
    print('Contains',c,'digit')
else:
    print("Doesn't contain digit")