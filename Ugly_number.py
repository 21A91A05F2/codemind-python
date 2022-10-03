n = int(input())
k = 0
while n!=1:
    if n%2==0:
        n//=2
    elif n%3==0:
        n//=3
    elif n%5==0:
        n//=5
    else:
        k+=1
        break
if k==0:
    print("Ugly Number")
else:
    print("Not Ugly Number")