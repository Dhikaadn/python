import random
import time
n = int(input("masukan saldo awal: "))
m = int(input("masukan pulsa yang diinginkan mama: "))
sukses = 0
if n>=m:
    t=int(input("masukan tanggal lahir mama: "))
    if t==12:
        for i in range(3):
            r=random.random()
            if(r>0.5):
                print("Tranksaksi berhasil")
                sukses = 1
                break
            print("mohon tunggu")
            time.sleep(1)
        if sukses==0:
            print("tranksaksi gagal")
    else:
        print("ini penipu")
else:
    print("saldo tidak cukup")
