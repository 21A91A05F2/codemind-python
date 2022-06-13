


t=int(input())
x=0
for i in range(t):
    s=input()
    for j in range(len(s)-1):
        if s[j]=='+' and s[j+1]=='+':
            x+=1
        elif s[j]=='-' and s[j+1]=='-':
            x-=1
print(x)