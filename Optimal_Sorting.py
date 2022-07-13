t=int(input())
while(t):
    n=int(input())
    a=list(map(int,input().split()))
    def sort(a):
        n=len(a)
        if n==1 or n==0:
            return 1
        return a[0]<=a[1] and sort(a[1:])
    if sort(a):
        print("0")
    else:
        m=max(a)
        l=min(a)
        o=m-l
        print(o)
    t-=1