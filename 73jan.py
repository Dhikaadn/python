print("Menghitung Luas Segitiga dengan Fungsi")
def LuasSegitiga(a,t):
	luas=0.5*a*t
	return luas

def main():
	a = int(input("Masukan alas: "))
	b = int(input("Masukan tinggi: "))
	print("luasnya: ",LuasSegitiga(a,b))
main()

