
arr=list(map(int,input().split()))
n=len(arr)
k=0
v=0;m=0
for i in range(0,n):
    for j in range(0,n):
        if i!=j:
            if arr[i]*arr[j]>k:
                k=arr[i]*arr[j]
                v=i
                m=j
print((arr[v]-1)*(arr[m]-1)) 