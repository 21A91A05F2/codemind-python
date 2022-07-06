n=int(input())
a=list(map(int,input().split()))
n2=int(input())
a2=list(map(int,input().split()))
c=0
for i in a:
    if i in a2:
        c+=1
if c==n:
    print('True')
else:
    print('False')