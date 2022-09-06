def fun(n):
    if n<0:
        print("Incorrect Expression")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fun(n-1)+fun(n-2)
n = int(input())
for i in range(n):
    print(fun(i),end=" ")