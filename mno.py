n = int(input("masukkan bilangan: "))
if (n>0) and (n%2==0):
    print("Positif Genap")
elif (n>0) and (n%2!=0):
    print("Positif Ganjil")
elif (n<0) and (n%2==0):
    print("Negatif Genap")
elif (n<0) and (n%2!=0):
    print("Negatif Ganjil")
else:
    print("nol")
    
