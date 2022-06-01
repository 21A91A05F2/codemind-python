def count(st):
    c=1
    for i in range(1,len(st)-1):
        if (st[i].isupper()):
            c+=1
    
    return c


st=input()
print(count(st))        
