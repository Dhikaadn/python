print("\t\t\t   Program Penjualan Susu")
nm = str(input("Masukan nama pembeli: "))
ks = int(input("Masukan kode Susu [1/2/3]: "))
ku = str(input("Masukan Kode Ukuran [S/M/L]: "))
jb = int(input("Masukan Jumlah Beli: "))

if(ks==1):
    print("Indomilk")
    if(ku=="S"):
        hr = (5000)
    elif(ku=="M"):
        hr = (7500)
    elif(ku=="L"):
        print(9500)
elif(ks==2):
    print("Dancow")
    if(ku=="S"):
        hr = (4500)
    elif(ku=="M"):
        hr = (6500)
    elif(ku=="L"):
        hr = (8500)
elif(ks==3):
    print("Sustagen"):
        if(ku=="S"):
            hr = (9500)
        elif(ku=="M"):
            hr = (15500)
        elif(ku=="L"):
            hr = (19500)

jp
            
                
        
