n=int(input())
a=list(map(int,input().split()))
a.sort()
num=1
for i in a:
    if i==num:
        num=num+1
else:
    print(num)