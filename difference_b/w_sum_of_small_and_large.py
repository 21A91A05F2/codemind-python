s=input()
mn,mx=0,0
l=list(s.split(" "))
for i in l:
    mn+=ord(min(i))
    mx+=ord(max(i))
print(abs(mx-mn))