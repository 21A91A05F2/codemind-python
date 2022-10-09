n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,n,2):
    if i==n-1:
        break
    elif l[i]>l[i-1] and l[i]>l[i+1]:
        c+=1
    else:
        print(-1)
        exit()
print(c)