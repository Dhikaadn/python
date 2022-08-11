print("No 1")
a = "Hello world"
n = int(input("Berapa kali: "))
def TampilkanBerapaKali(a,n):
	for i in range(n):
		print(a)
def main():
	TampilkanBerapaKali(a,n)
	
main()

print("No 2")
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
print("No 3")
def LuasSegitiga(a,t):
	luas=0.5*a*t
	return luas

def main():
	c = int(input("Masukan alas: "))
	d = int(input("Masukan tinggi: "))
	print("luasnya: ",LuasSegitiga(c,d))
main()

print("No 4")
def CariGenap(n):
	genap = 0
	for element in n:
		if(int(element)%2==0):
			genap+=1
	return genap
	
n = input("Masukan angka: ").split(" ")
print("Banyaknya angka genap: ", CariGenap(n))

print("No 5")
def CariKembar(n):
	kembar = {}
	for element in n:
		jml = 0
		jml = n.count(element)
		if jml>1:
			kembar[element]=jml
	return kembar
	
n = input("Masukan angka: ").split(" ")
kembar = CariKembar(n)
for key in kembar:
	print(f'angka {key} kembar,berjumlah{kembar[key]}')
	
print("No 6")
def jumlah(n):
	total = 0
	for element in n:
		total+=int(element)
	return total
	
n = input('Masukan angka:').split(' ')
print('Jumlah:',jumlah(n))

print("No 7")
def aritmetika(a,b,c):
	lst=[]
	for i in range(a,b,c):
		lst.append(i)
	return lst
awal = 1
akhir = 20
sls = 2
deret = aritmetika(awal,akhir,sls)
print("Deret: ",deret)
