s=input()
v= 0
c= 0 
d=0
k=0
s = s.lower();  
for i in range(0,len(s)):   
    if s[i] in ('a',"e","i","o","u"):  
        v= v+ 1;  
    elif (s[i] >= 'a' and s[i] <= 'z'):  
        c= c+ 1;  
    elif s[i].isdigit():
        d=d+1
    else:
        k=k+1
  
print("Vowels:",v)  
print('Consonants:',c) 
print('Digits:',d) 
print('White spaces:',k)  