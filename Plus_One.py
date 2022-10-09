n=int(input())
l=list(map(int,input().split()))
s=""
for i in l:
    s+=str(i)
s=int(s)+1
k=list(str(s))
print(*k)