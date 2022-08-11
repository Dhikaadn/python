print("Menghitung Selisih Waktu")
def detik(jam,menit,detik):
	return(jam*3600)+(menit*60)+detik

print("Jam awal : ")
jamA = int(input("jam(hh) : "))
menitA = int(input("menit(mm) : "))
detikA = int(input("detik(dd) : "))

print("Jam akhir : ")
jamB = int(input("jam(hh) : "))
menitB = int(input("menit(mm) : "))
detikB = int(input("detik(dd) : "))

awal = detik(jamA,menitA,detikA)
akhir = detik(jamB,menitB,detikB)
selisih = akhir - awal

jam = selisih//3600
sisa = selisih - 3600*jam
menit = sisa//60
detik = sisa - (60*menit)

print("selisih jam awal dan jam akhir adalah: ",str(jam).zfill(2)+":"+str(menit).zfill(2)+":"+str(detik).zfill(2))

# print("selisih jam awal dan jam akhir adalah %d jam %d menit %d detik" %(jam,menit,detik))



