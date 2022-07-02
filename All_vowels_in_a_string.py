myStr=input()
allVowels = set("aeiou")
myStr=set(myStr)

for char in myStr :
    if char in allVowels :
        allVowels.remove(char)
if len(allVowels) == 0:
    print("True")
else :
    print("False")