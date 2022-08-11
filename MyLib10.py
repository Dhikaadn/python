def panjangString(s):
 # mengebalikan integer panjang string
 # gunakan teknik penjumlahan sum, gunakan jenis pengulangan yang sesuai
 # boleh melakukan pengulangan string seperti ini: for char in string:
 # mulai disini (sekitar 4-7 baris kode) 20 point
	counter = 0
	for c in s:
		counter=counter+1
	return counter
 #berhenti disini
def cariKarakter(c,s): # ini prosedur, outputkan “ada” atau “tidak ada”
 # boleh memanfaatkan fungsi panjangString atau
 # boleh melakukan pengulangan string seperti ini: for char in string:
 # boleh membuat variabel boolean untuk menampung jika karakter ketemu
 # jika karakter c sama dengan salah satu karakter pada string s
 # jika variabel penampung sebelumnya bernilai True maka outputkan “ada”
 # jika masih False maka outputkan “tidak ada”
 # mahasiswa boleh menggunakan alur yang lain
 # yang penting output dari prosedur ini “ada” jika ketemu
 # “tidak ada” jika tidak ketemu
 # mulai disini (sekitar 8-15 baris) 20 point
    		
 #berhenti disini
	ketemu=False
	for i in s:
		if c==i:
			print("ada")
			ketemu=True
			break
	if ketemu==False:
		print("tidak ada")
def frekuensiKarakter(c,s): #  mengembalikan integer frekuensi karakter
 # idenya sederhana lakukan pengulangan dan pengecekan di setiap karakter
 # gunakan teknik penjulahan sum
 # jika setiap karakter pada string s sama dengan karakter c maka sum + 1
 # kembalikan sum
 # mulai disini (sekitar 4-6 baris kode) 20 point
	counter=0
	for i in s:
		if c==i:
			counter=counter+1
	return counter
	
 #berhenti disini
def cekPalindrom(s): # mengembalikan boolean True atau False
 # disini idenya adalah kita harus memiliki string s yang sudah di balik
 # cara membalikanya dengan string slicing s[start:stop:step]
 # lihat catatan ppt
 # tidak perlu ada pengulangan, hanya pengecekan
 # jika s sama dengan s yang sudah di balik maka mengembalikan True
 # jika tidak False
 # mulai disini (sekitar 1 sampai 5 baris kode) 20 point
	return s==s[::-1]
 #berhenti disini
