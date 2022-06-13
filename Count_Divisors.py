x,y,d=map(int,input().split())
c=0
for i in range(x,y+1):
    if(i%d==0):
        c+=1
print(c)