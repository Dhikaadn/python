# Judul
# Menentukan Bilangan Ganjil dan Genap

# Kamus
# n : integer

# Deskripsi
# input n
# if(bilangan genap)then
# {bilangan genap}
# else(bilangan ganjil)then
# {bilangan ganjil}

#Menentukan Bilangan Ganjil dan Genap

#kamus
n = int

#deskripsi
n = int(input("masukkan angka : "))

if n%2==0:
    print("bilangan genap")
elif n%2!=0:
    print("bilangan ganjil")
else:
    print("nol")
