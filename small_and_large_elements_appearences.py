
s=input()
s="".join(list(s.split(" ")))
print(min(s),s.count(min(s)),end=" ")
print(max(s),s.count(max(s)),end=" ")