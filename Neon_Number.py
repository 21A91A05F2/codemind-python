
a=int(input())
p=a*a
s=0
while p!=0:
    r=p%10
    s+=r
    p=p//10
if s==a:
    print("Neon Number")
else:
    print("Not Neon Number")