# Program: Pendataan Barang
import prak5
# Kamus
print("Masukkan kapasitas barang:",end=" ")
n = int(input())
arrId = [int]*n
arrBarang = [str]*n
arrHarga = [int]*n

menu="1"
# Algoritma
while menu !="0":
    print("Kapasitas Barang:",n)
    print("Pilih Menu (Ketik 1/2/3 dan 0 untuk keluar")
    print("1. Input Data")
    print("2. Lihat Data")
    print("3. Lihat Data Terurut")
    print("Ketikkan:",end="")
    menu=input()
    if menu == "1":
        for i in range(n):
            print("Data ke-",i+1)
            arrId[i]=int(input("Masukkan id: "))
            arrBarang[i]=input("Masukkan nama barang: ")
            arrHarga[i]=int(input("Masukkan harga: "))
        prak5.InputData(arrId,arrBarang,arrHarga,n)
    elif menu == "2":
        prak5.LihatData(n)
    elif menu == "3":
        prak5.LihatDataTerurut(n)
    elif menu == "0":
        break
