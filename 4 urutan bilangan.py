a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
if(a>b)and(a>c)and(a>d):
    print(a)
    if(b>c)and(b>d):
        print(b)
        if(c>d):
            print(c)
            print(d)
        else:
            print(d)
            print(c)
    elif(c>b)and(c>d):
        print(c)
        if(b>d):
            print(b)
            print(d)
        else:
            print(d)
            print(b)
    else:
        print(d)
        if(b>c):
            print(b)
            print(c)
        else:
            print(c)
            print(b)

elif(b>c)and(b>d)and(b>a):
    print(b)
    if(c>d)and(c>a):
        print(c)
        if(d>a):
            print(d)
            print(a)
        else:
            print(a)
            print(d)
    elif(d>a)and(d>c):
        print(d)
        if(a>c):
            print(a)
            print(c)
        else:
            print(c)
            print(a)
    else:
        print(a)
        if(d>c):
            print(d)
            print(c)
        else:
            print(c)
            print(d)

elif(c>a)and(c>b)and(c>d):
    print(c)
    if(a>b)and(a>d):
        print(a)
        if(b>d):
            print(b)
            print(d)
        else:
            print(d)
            print(b)
    elif(b>d)and(b>a):
        print(b)
        if(d>a):
            print(d)
            print(a)
        else:
            print(a)
            print(d)
    else:
        print(d)
        if(a>b):
            print(a)
            print(b)
        else:
            print(b)
            print(a)

else:
    print(d)
    if(a>b)and(a>c):
        print(a)
        if(b>c):
            print(b)
            print(c)
        else:
            print(c)
            print(b)
    elif(b>a)and(b>c):
        print(b)
        if(a>c):
            print(a)
            print(c)
        else:
            print(c)
            print(a)
    else:
        print(c)
        if(a>b):
            print(a)
            print(b)
        else:
            print(b)
            print(a)
                    
    
    
        
        
