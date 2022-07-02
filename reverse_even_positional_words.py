n=input()
x=n.split()

for i in range(len(x)):
    if i%2==0:
        p=str(x[i])
        print(p[::-1],end=' ')
    else:
        p=str(x[i])
        print(p,end=' ')