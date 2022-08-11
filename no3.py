Judul
Menentukan Urutan Nilai Terbesar ke Terkecil

Kamus
bil_a,bil_b,bil_c : integer

Deskripsi
input bil_a
input bil_b
input bil_c
if (bil_a>bil_c and bil_a>bil_b):then
    if (bil_b>bil_c):then
        output{bil_a,bil_b,bil_c}
    else:then
        output{bil_a,bil_c,bil_b}
elif (bil_b>bil_a and bil_b>bil_c):then
    if (bil_a>bil_c):then
        output{bil_b,bil_a,bil_c}
    else:then
        output{bil_b,bil_c,bil_a}
elif (bil_b>bil_a and bil_c>bil_b):then
    if (bil_a>bil_b):then
        output{bil_c,bil_a,bil_b}
    else:then
        output{bil_c,"-",bil_b,bil_a}

#Menentukan Urutan Nilai Terbesar ke Terkecil

#kamus
bil_a,bil_b,bil_c = integer

#deskripsi
bil_a = int(input("masukan a: "))
bil_b = int(input("masukan b: "))
bil_c = int(input("masukan c: "))
if (bil_a>bil_c and bil_a>bil_b):
    if (bil_b>bil_c):
        print("urutan terbesar ke terkecil",bil_a,bil_b,bil_c)
    else:
        print("urutan terbesar ke terkecil",bil_a,bil_c,bil_b)
elif (bil_b>bil_a and bil_b>bil_c):
    if (bil_a>bil_c):
        print("urutan terbesar ke terkecil",bil_b,bil_a,bil_c)
    else:
        print("urutan terbesar ke terkecil",bil_b,bil_c,bil_a)
elif (bil_c>bil_a and bil_c>bil_b):
    if (bil_a>bil_b):
        print("urutan tebesar ke terkecil",bil_c,bil_a,bil_b)
    else:
        print("urutan terbesar ke terkecil",bil_c,bil_b,bil_a) 
        
