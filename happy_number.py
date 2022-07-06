
n=int(input())
while sum!=1 and sum!=4:
    sum=0
    while n>0 :
        temp=n%10;
        sum=sum+(temp*temp);
        n=n//10;
    n=sum;
    
if sum==1:
    print("True");
else:
    print("False");