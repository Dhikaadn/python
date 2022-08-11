n = int(input("masukan: "))
#bil prima harus lebih dari 1
if n > 1:
    for i in range(2,n):
        if(n%i)==0:
            print("bukan bil primaa")
            break
    else:
        print("bil prima")
else:
    print("jelas bukan prima")
