print("Penjumlahan")
def jumlah(n):
	total = 0
	for i in n:
		total+=int(i)
	return total
	
n = input('Masukan angka:').split(' ')
print('Jumlah:',jumlah(n))