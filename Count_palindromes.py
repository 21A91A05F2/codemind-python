def ispali(i):
    k=str(i)
    if i==int(k[::-1]):
        return True
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if ispali(i):
        c+=1
print(c)