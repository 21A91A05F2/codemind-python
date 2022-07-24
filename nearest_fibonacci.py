def fabio(n):
    if (n==0):
        print('0')
        return
    f=0
    s=1
    t=f+s
    while(t<=n):
        f=s
        s=t
        t=f+s
    if (abs(t-n)>abs(s-n)):
        print(s)
    elif (abs(t-n)<abs(s-n)):
        print(t)
    else:
        print(s,t,end=" ")

if __name__ == '__main__':
    n=int(input())
    fabio(n)