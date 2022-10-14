
n = int(input())
arr = list(map(int,input().split()))
e = []
o = []
for i in range(0,n):
    if arr[i]%2==0:
        e.append(arr[i])
    else:
        o.append(arr[i])
i = 0
j = 0
while i<len(o) or j<len(e):
    if i<len(o):
        print(o[i],end=" ")
        i+=1
    if j<len(e):
        print(e[j],end=" ")
        j+=1
if n%2!=0:
    print("0")