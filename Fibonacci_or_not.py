n=int(input())
c=0
n1,n2=0,1
if n==1 or n==0:
    print("True")
else:
    while c<n:
        c=n1+n2
        n1=n2
        n2=c
    if c==n:
        print('True')
    else:
        print('False')