#Mengonversikan detik ke suatu waktu
x = int(input("Masukkan angka(waktu): "))#menginput integer
hh = x // 3600#menghitung jam
sisadetik = x % 3600#perhitungan sisa detik dengan modulo
mm = sisadetik // 60#menghitung menit
ss = sisadetik % 60#menghitung detik
print("%d detik sama dengan %d:%d:%d" %(x,hh,mm,ss))#output
