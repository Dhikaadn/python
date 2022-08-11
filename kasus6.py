#Kamus
awal = int(input("Masukan Saldo Awal:"))
sisa = awal
#Algoritma
while True:
    pengeluaran = int(input("Masukan Pengeluaran hari ini(-1 untuk keluar):"))
    # sisa = sisa - pengeluaran
    if pengeluaran == -1:
        print("Sisa saldo = ", sisa)
        break
    elif sisa > pengeluaran:
        sisa -= pengeluaran
    else:
        print("Saldo tidak cukup")
        print("Sisa saldo ", sisa)
        break 