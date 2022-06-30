a=int(input())
rev=0
while a>0:
    r=a%10
    rev=10*rev+r
    a=a//10
print(rev)