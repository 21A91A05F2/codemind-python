n = int(input())
l = list(map(int,input().split()))
d = []
for i in range(n):
    if l[i] not in d:
        d.append(l[i])
print(*d)
        
    