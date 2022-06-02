n=int(input())
c=0;s=0;
temp=n
while n>0:
    r=n%10
    n//=10
    c+=1
n=temp
while n>0:
    r=n%10
    s=s+pow(r,c)
    n=n//10
    c-=1
if s==temp:
    print("True")
else:
    print("False")
