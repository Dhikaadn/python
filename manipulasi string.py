#Deskrispsi
a = "UNIVERSITAS DIAN NUSWANTORO"
b = "MAGERSARI"
x = 1
#Tampilkan String
print(a)
print(b)

#Panjang String
print("Panjang string a : ",len(a))
print("Panjang string b : ",len(b))

#Karakter Ganjil
#var a
print("Karakter genap variabel a =", end=" ")
for i in a:
    if(x%2 == 0):
        print(i, end=" ")
    x = x + 1
print()
x = x + 1

#var b
print("Karakter ganjil variabel b =", end=" ")
for i in b:
    if(x%2 != 0):
        print(i, end=" ")
    x = x + 1
print()
x = x + 1

#Jumlah A
print("Jumlah A pada variabel a : ",a.count("A"))
print("Jumlah A pada variabel b : ",b.count("A"))

# Jumlah Vokal
va = a.count("A")+a.count("I")+a.count("U")+a.count("E")+a.count("O")
vb = b.count("A")+b.count("I")+b.count("U")+b.count("E")+b.count("O")
print("Jumlah vokal pada variabel a : ",va)
print("Jumlah vokal pada variabel b : ",vb)

# Jumlah Kata
kata_a = a.split()
kata_b = b.split()
print("Jumlah kata pada variabel a : ",len(kata_a))
print("Jumlah kata pada variabel b : ",len(kata_b))

#Membalik Kata
a1 = "UNIVERSITAS"
b1 = "MAGERSARI"
print("Kebalikan kata pertama UNIVERSITAS adalah ",a1[::-1])
print("Kebalikan kata pertama MAGERSARI adalah ",b1[::-1])

