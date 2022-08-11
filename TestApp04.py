from mylib04 import*

def main():
    x = int(input("Masukkan angka pertama: "))
    y = int(input("Masukkan angka kedua: "))
    z = int(input("Masukkan angka ketiga: "))
    q = int(input("Masukkan angka keempat: "))
    print("Tambah: ",tambah(x,y,z,q))
    print("Kurang: ",kurang(x,y,z,q))
    print("Kali: ",kali(x,y,z,q))
    print("Bagi: ",bagi(x,y,z,q))
    banding(x,y,z,q)
main()

