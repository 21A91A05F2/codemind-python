s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
for i in s1:
    if i not in s2:
        print(False)
        break
else:
    print(True)