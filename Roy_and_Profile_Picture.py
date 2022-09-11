l = int(input())
for _ in range(int(input())):
    w,h = map(int,input().split())
    if w<l or h<l:
        print("UPLOAD ANOTHER")
    else:
        if (w>=l and h>=l) and w==h:
            print("ACCEPTED")
        else:
            print("CROP IT")

    