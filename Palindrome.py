n=int(input())
v=0
temp=n
while(n>0):
    r=n%10
    v=v*10+r
    n=n//10
if v==temp:
    print("True")
else:
    print("False")