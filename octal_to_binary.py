o=int(input())
i=0;d=0;b=0;
while o:
    d+=(o%10)*pow(8,i)
    o//=10
    i+=1
i=1
while d:
   b+=(d%2)*i
   d//=2
   i*=10 
print(b)