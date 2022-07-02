
  
Num = int(input())
Sum = 0
Temp = Num
 
while(Temp > 0):
    Factorial = 1
    i = 1
    Reminder = Temp % 10
 
    while(i <= Reminder):
        Factorial = Factorial * i
        i = i + 1
    Sum = Sum + Factorial
    Temp = Temp // 10
     
if (Sum == Num):
    print("The number %d is a strong number" %Num)
else:
    print("The number %d is not a strong number" %Num)