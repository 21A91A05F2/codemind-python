s=input()
otp=""
for i in s:
    if int(i)%2!=0:
        otp+=str(int(i)**2)
print(otp)