def detik(jam,menit,detik):
	return(jam*3600)+(menit*60)+detik

print("Jam awal : ")
jamA = eval(input("jam : "))
menitA = eval(input("menit : "))
detikA = eval(input("detik : "))

print("Jam akhir : ")
jamB = eval(input("jam : "))
menitB = eval(input("menit : "))
detikB = eval(input("detik : "))

awal = detik(jamA,menitA,detikA)
akhir = detik(jamB,menitB,detikB)
selisih = akhir - awal

jam = selisih//3600
sisa = selisih - 3600*jam
menit = sisa//60
detik = sisa - (60*menit)

print("selisih jam awal dan jam akhir adalah %d jam %d menit %d detik" %(jam,menit,detik))



