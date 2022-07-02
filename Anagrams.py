str1 = input()
str2 = input()

str1 = str1.lower()
str2 = str2.lower()

if(len(str1) == len(str2)):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    if(sorted_str1 == sorted_str2):
        print("True")
    else:
        print("False")

else:
    print("False")
