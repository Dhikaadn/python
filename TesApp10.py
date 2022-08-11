from MyLib10 import *
def main():
	data = "balonku ada lima, rupa-rupa warnanya"
	print("data: ",data)
	# buat inputan untuk variabel c1,c2, dan p
	c1 = input()
	c2 = input()
	p = input()

	#buat output untuk
	# 1. panjangString dengan parameter aktual data
	# 2. cariKarakter dengan parameter aktual data dan c1
	# 3. frekuensiKarakter dengan paramter aktual data dan c2
	# 4. Pengecekan if else biasa jika cekPalindrom(P) bernilai True
	# outputkan “palindrom”
	# jika tidak outputkan “bukan palindrom”
	# 20 point
	print(panjangString(data))
	cariKarakter(c1,data)
	print(frekuensiKarakter(c2,data))
	if cekPalindrom(p):
		print("palindrom")
	else:
		print("bukan palindrom")
if __name__ == "__main__":
 main()

