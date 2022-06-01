n=int(input())
a=list(map(int,input().split()))
odd=0;
for i in range(0,n):
    if a[i]%2!=0:
        odd+=1
if odd<=2:
    print("YES")
else:
    print("NO")
