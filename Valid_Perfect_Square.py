def sqrt(a):
    for i in range(1,int(a**0.5)+1):
        if i**2==a:
           
            return True
    else:
        return False
n=int(input())
while n:
    a=int(input())
    print(sqrt(a))
    n=n-1