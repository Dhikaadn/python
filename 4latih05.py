pjg = float(input("masukan panjang: "))
lbr = float(input("masukan lebar: "))
luas = float(pjg*lbr)
print("luas: ",luas)
persetujuan = str(input("persetujuan: "))
setuju = float(luas/2)
tidaksetuju = float(luas)
if(persetujuan=="setuju"):
    print(setuju)
elif(persetujuan=="tidak setuju"):
    print(tidaksetuju)
