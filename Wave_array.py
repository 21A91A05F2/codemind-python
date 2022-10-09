
n=int(input())
l=list(map(int,input().split()))
if l[0]<l[1]:
    for i in range(1,n,2):
        if n%2==0 and i==n-1 :
            if l[i-1]>l[i]:
                print("no")
                break
        elif l[i-1]>l[i] or l[i+1]>l[i]:
            print("no")
            break
    else:
        print("yes")
else:
    for i in range(1,n,2):
        if n%2==0 and i==n-1 :
            if l[i-1]<l[i]:
                print("no")
                break
        elif l[i-1]<l[i] or l[i+1]<l[i]:
            print("no")
            break
    else:
        print("yes")