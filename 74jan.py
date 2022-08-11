print("Mencari Bilangan Genap")
def CariGenap(n):
	genap = 0
	for i in n:
		if(int(i)%2==0):
			genap+=1
	return genap
	
n = input("Masukan angka: ").split(" ")
print("Banyaknya angka genap: ",CariGenap(n))
	