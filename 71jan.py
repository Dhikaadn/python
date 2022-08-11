print("Mencetak Hello world Sebanyak n kali")
a = "Hello world"
n = int(input("Berapa kali: "))
def TampilkanBerapaKali(a,n):
	for i in range(n):
		print(a)
def main():
	TampilkanBerapaKali(a,n)
	
main()

