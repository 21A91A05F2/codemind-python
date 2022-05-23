n=int(input())
sq=n*n
flag=1
while n:
    if(sq%10!=n%10):
        flag=0
        break
    n//=10
    sq//=10
if(flag==1):
    print("Automorphic Number")
if(flag==0):
    print("Not an Automorphic Number")