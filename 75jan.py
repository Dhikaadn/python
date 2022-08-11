print("Mencari Angka Kembar")
def CariKembar(n):
	kembar = {}
	for i in n:
		jml = 0
		jml = n.count(i)
		if jml>1:
			kembar[i]=jml
	return kembar
	
n = input("Masukan angka: ").split(" ")
kembar = CariKembar(n)
for a in kembar:
	print(f'angka {a} kembar,berjumlah{kembar[a]}')
	