t=int(input())
c=0
for _ in range(t):
    c=0
    n,m = map(int,input().split())
    for i in range(n,m+1):
        a=i%10
        if a==2 or a==3 or a==9:
            c+=1
    print(c)    
        