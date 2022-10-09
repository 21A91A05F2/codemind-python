s=input()
s=s.lower()
c=0
al="aeiou"
a,b=0,len(s)-1
while a<b:
    if s[a].isalpha() and s[b].isalpha():
        if ( s[a] in al and s[b] not in al) or (s[a] not in al and s[b] in al):
            c+=1
    a+=1
    b-=1
print(c)