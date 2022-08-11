uang = int(input("Masukan jumlah uang sakumu sayang: "))
if(1700000<=uang<2200000):
    print("bisa nonton konser dengan tiket reguler")
elif(uang>=2200000):
    print("bisa nonton konser tiket vip")
elif(1200000<uang<1700000):
    print("uang tidak cukup")
else:
    print("tidak valid")
