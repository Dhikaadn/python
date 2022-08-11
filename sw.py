n = int(input("Masukan angka: "))
if n>0 and n%2==0:
    print("Positif genap")
elif n>0 and n%2!=0:
    print("Positif ganjil")
elif n<0 and n%2==0:
    print("Negatif genap")
elif n<0 and n%2!=0:
    print("Negatif ganjil")
else:
    print("nol")
