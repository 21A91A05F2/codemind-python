
s=list(map(str,input().split( )))
c=0
al="aeiou"
for i in s:
    i=i.lower()
    a,b=0,len(i)-1
    while a<b:
        if ( i[a] in al and i[b] not in al ) or ( i[a] not in al and i[b] in al ):
          c+=1
        a+=1
        b-=1
print(c)
       