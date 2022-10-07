def ispalin(n):
    t=n
    r=0
    while(n>0):
        d=n%10
        r=r*10+d
        n=n//10
    if t==r:
        return r
    return False
n = int(input())
f,b = n+1,n-1
while not ispalin(f) and not ispalin(b):
    f+=1
    b-=1
if ispalin(f) and ispalin(b):
    fn,bn = abs(f-n),abs(b-n)
    if fn==bn:
        print(b,f)
    else:
        if abs(f-n)>abs(b-n):
            print(f)
        else:
            print(n)
elif ispalin(f):
    print(f)
else:
    print(b)