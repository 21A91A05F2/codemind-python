n=int(input())
temp=n
x=0
while temp!=1:
    if temp%2==0:
        temp/=2
    elif temp%3==0:
        temp/=3
    elif temp%5==0:
        temp/=5
    else:
        print("Not Ugly Number")
        x=1
        break
if x==0:
    print("Ugly Number")
        