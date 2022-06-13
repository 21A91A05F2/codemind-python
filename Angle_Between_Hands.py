l=input().split(':')
h=int(l[0])
m=int(l[1])
a=abs((h*30)-(11*m)/2)
if(a<360-a):
    if(a>int(a)):
        print("%.1f" %a)
    else:
        print("%.1f" %a)
else:
    x=float(360-a)
    if(x>int(x)):
        print("%.1f" %x)
    else:
        print("%.1f" %x)