s=input()
c=0
for i in range(0,len(s)):
    if (s[i]>='0' and s[i]<='9'):
        c=c+int(s[i])
print(c)