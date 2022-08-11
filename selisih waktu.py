def detik(jam,menit,detik):
    return(jam*3600)+(menit*60)+detik

print("Jam tidur : ")
jamA = eval(input("jam : "))
menitA = eval(input("menit : "))
detikA = eval(input("detik : "))

print("Jam bangun : ")
jamB = eval(input("jam : "))
menitB = eval(input("menit : "))
detikB = eval(input("detik : "))

tidur = detik(jamA,menitA,detikA)
bangun = detik(jamB,menitB,detikB)
selisih = bangun - tidur

jam = selisih//3600
sisa = selisih - 3600*jam
menit = sisa//60
detik = sisa - (60*menit)

print("selisih jam bangun dan jam tidur adalah %d jam %d menit %d detik" %(jam,menit,detik))
