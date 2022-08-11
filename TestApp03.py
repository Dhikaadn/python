from mylib03 import*

def main():
    x = int(input("Masukkan angka pertama: "))
    y = int(input("Masukkan angka kedua: "))
    print("Tambah: ",tambah(x,y))
    print("Kurang: ",kurang(x,y))
    print("Kali: ",kali(x,y))
    print("Bagi: ",bagi(x,y))
    banding(x,y)
main()

