n=int(input())
rev1=0
rev2=0
s=n**2
while(n):
    r=n%10
    n=n//10
    rev1=rev1*10+r
sq=rev1**2
while(sq):
    m=sq%10
    sq=sq//10
    rev2=rev2*10+m
if(s==rev2):
    print("True")
else:
    print("False")