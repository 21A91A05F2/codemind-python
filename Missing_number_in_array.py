
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(1,n+1):
        if i not in a:
            print(i)