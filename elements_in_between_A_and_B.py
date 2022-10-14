
n = int(input())
arr = list(map(int,input().split()))
a,b = map(int,input().split())
c =[]
for i in range(n):
    if arr[i]>=a and arr[i]<=b:
       c.append(arr[i])
if len(c)==0:
    print("-1")
else:
    print(*c)