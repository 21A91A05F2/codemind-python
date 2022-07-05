
n=int(input())
arr=list(map(int,input().split()))
res=0
x=0
y=0
for i in range(0,n,4):
    x=x+arr[i]
for i in range(2,n,4):
    y=y+arr[i]
for i in range(1,n,4):
    x=x+arr[i]
for i in range(3,n,4):
    y=y+arr[i]
res=abs(x-y);
if res%4==0:
    print("X")
else:
    print("Y")