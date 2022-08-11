a=17

b=0

i=1

sum=0

while a>2:
    p=a/b
    if(i%2 == 0):
        p=p*-1
        tnd="-"
    else:
        p=p*1
        tnd="+"

    sum=sum+p
    print(tnd,a,"/",b,end=" ")
    a=a-2
    b=b+2
    i=i+1
print("=",sum)
