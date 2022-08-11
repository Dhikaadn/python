p = float(input("masukan panjang: "))
l = float(input("masukan panjang: "))
luas = p*l
print("luas: ",luas)
persetujuan = str(input("persetujuan: "))
setuju = (p*l)/2
tidaksetuju = p*l
if(persetujuan=="setuju"):
        print(setuju)
elif(persetujuan=="tidaksetuju"):
        print(tidaksetuju)
