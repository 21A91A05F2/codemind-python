a,b=map(int,input().split())
for i in range (1,b+1):
    p=a*i
    if i%2==0:
        continue
    print(a,'x',i,'=',p)