n = int(input())
arr = list(map(int,input().split()))
a,b = map(int,input().split())
p=[]
for i in range(n):
    if arr[i]>=a and arr[i]<=b:
        p.append(arr[i])
if len(p)==0:
    print("-1")
else:
    print(*p)