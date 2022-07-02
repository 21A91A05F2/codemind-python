
def addDigits(num):
    if len(str(num))==1:
        return num
    while True:
        l = [int(i) for i in str(num)]
        num = sum(l)
        if len(str(num))==1:
            return num
num=int(input())
print(addDigits(num))