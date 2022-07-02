num=int(input())
sum=0
product=1
num1 = num
 
while(num>0):
    d=num%10
    sum=sum+d
    product=product*d
    num=num//10
 
if(sum==product):
    print("Spy Number")
else:
    print("Not Spy Number")
