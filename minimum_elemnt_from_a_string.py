s=list(map(str,input().split( )))
m=min(s[-1])
if ord(m)<97:
    if chr(ord(m)+32) in s[-1]:
        print(chr(ord(m)+32))
    else:
        print(m)
else:
    print(m)