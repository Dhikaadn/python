n = str(input("masukan jenjang/prodi/fakultas: "))
doktoral = ("Ilmu Komputer(FIK)")
pascasarjana = ("Magister Manajemen(FEB),Magister Teknik Informatika(FIK)")
sarjana = ("teknik Informatika, Sistem Informasi, DKV, Ilkom (FIK) Akuntansi Manajemen (FEB),English, Jepang (FIB),Kesehatan Masyarakat, Kesehatan Lingkungan (FKM),Eletro, Industri, Biomedis (FT)")
diploma4 = ("Animasi, Televisi (FIK),Perhotelan (FIB)")
diploma3 =("Teknik Informatika, Broadcasting (FIK),Rekam Medis (FKM)")

ilmukomputer = ("Doktoral(FIK)")
magistermanajemen = ("Pasca Sarjana(FEB)")
magisterteknikinformatika = ("Pasca Sarjana(FIK)")
teknikinformartika_sisteminformasi_dkv_ilkom =("Sarjana(FIK)")
akuntansimanajemen = ("Sarjana(FEB)")
english_jepang = ("Sarjana(FIB)")
kesehatanmasyarakat_kesehatanlingkungan =("Sarjana(FKM)")
elektro_industri_biomedis = ("Sarjana(FT)")
animasi_televisi = ("Diploma 4(FIK)")
perhotelan = ("Diploma 4(FIB)")
teknikinformatika_broadcasting = ("Diploma 3(FIK)")
rekammedis = ("Diploma 3(FKM)")

fik = ("Doktoral: Ilmu Komputer\n"
       "Pasca Sarjana: Magister Teknik Informatika\n"
       "Sarjana: Teknik Informatika,Sistem Informasi,DKV,Ilkom\n"
       "Diploma 4: Animasi,Televisi\n"
       "Diploma 3: Teknik Informatika,Broadcasting\n")
feb = ("Pasca Sarjana: Magister Manajemen\n"
       "Sarjana: Akuntansi Manajemen\n")
fib = ("Sarjana: English,Jepang\n"
       "Diploma 4: Perhotelan\n")
fkm = ("Sarjana: Kesehatan Masyarakat,Kesehatan Lingkungan\n"
       "Diploma 3: Rekam Medis\n")
ft = ("Sarjana: Eletro,Industri,Biomedis")

       
if(n=="doktoral"):
    print(doktoral)
elif(n=="pascasarjana"):
    print(pascasarjana)
elif(n=="sarjana"):
    print(sarjana)
elif(n=="diploma4"):
    print(diploma4)
elif(n=="diploma3"):
    print(diploma3)
elif(n=="ilmukomputer"):
    print(ilmukomputer)
elif(n=="magistermanajemen"):
    print(magistermanajemen)
elif(n=="magisterteknikinformatika"):
    print(magisterteknikinformatika)
elif(n=="teknikinformartika_sisteminformasi_dkv_ilkom"):
    print(teknikinformartika_sisteminformasi_dkv_ilkom)
elif(n=="akuntansimanajemen"):
    print(akuntansimanajemen)
elif(n=="english_jepang"):
    print(english_jepang)
elif(n=="kesehatanmasyarakat_kesehatanlingkungan"):
    print(kesehatanmasyarakat_kesehatanlingkungan)
elif(n=="elektro_industri_biomedis"):
    print(elektro_industri_biomedis)
elif(n=="animasi_televisi"):
    print(animasi_televisi)
elif(n=="perhotelan"):
    print(perhotelan)
elif(n=="teknikinformatika_broadcasting"):
    print(teknikinformatika_broadcasting)
elif(n=="rekammedis"):
    print(rekammedis)
elif(n=="fik"):
    print(fik)
elif(n=="feb"):
    print(feb)
elif(n=="fib"):
    print(fib)
elif(n=="fkm"):
    print(fkm)
elif(n=="ft"):
    print(ft)
else:
    print("Tidak Valid")
 

