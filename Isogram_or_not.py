s=input()
for i in s:
    if s.count(i)>1:
        print(False)
        break
else:
    print(True)