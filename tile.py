ch='y'
while ch=='y':
    a=-1
    while a<1:
        a=int(input("enter the width (>0)"))
        if a<1:
            print("error",end=" ")
    b=-1
    while b<1:
        b=int(input("enter the height(>0)"))
        if b<1:
            print("error")
    up="/ \\"
    down="\\_/"
    upt=" _ "
    if a>0 and b>0:
        for j in range(a):

            print(upt,end=" ")
        print()
    for i in range(b):
        for j in range(a-1):

            print(up,end="_")
        print(up,end=" ")
        print()
        for j in range(a-1):
            print(down,end=" ")
        print(down,end="")
        print()

    ch=input("enter for next input (y/n)")
