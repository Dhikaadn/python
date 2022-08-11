Judul
Menentukan Inputan Jenjang dan Fakultas

Kamus
jenjang : string
doktoral : Ilmu Komputer(FIK)
pasca sarjana : Magister Manajemen(FEB),Magister Teknik Informatika(FIK)
sarjana : teknik Informatika, Sistem Informasi, DKV, Ilkom (FIK) Akuntansi Manajemen (FEB),English, Jepang (FIB),Kesehatan Masyarakat, Kesehatan Lingkungan (FKM),Eletro, Industri, Biomedis (FT)
diploma4 : Animasi, Televisi (FIK),Perhotelan (FIB)
diploma3 : Teknik Informatika, Broadcasting (FIK),Rekam Medis (FKM)

Deskripsi
input jenjang
input fakultas
if(jenjang=="doktoral"):then
output{doktoral}
elif(jenjang=="pascasarjana"):then
output{pascasarjana}
elif(jenjang=="sarjana"):then
output{sarjana}
elif(jenjang=="diploma4"):then
output{diploma4}
elif(jenjang=="diploma3"):then
output{diploma3}
else:
output{"Tidak Valid"}

#Menentukan Inputan Jenjang dan Fakultas

#Kamus
jenjang = str
doktoral = Ilmu Komputer(FIK)
pascasarjana = Magister Manajemen(FEB),Magister Teknik Informatika(FIK)
sarjana = teknik Informatika, Sistem Informasi, DKV, Ilkom (FIK) Akuntansi Manajemen (FEB),English, Jepang (FIB),Kesehatan Masyarakat, Kesehatan Lingkungan (FKM),Eletro, Industri, Biomedis (FT)
diploma4 = Animasi, Televisi (FIK),Perhotelan (FIB)
diploma3 = Teknik Informatika, Broadcasting (FIK),Rekam Medis (FKM)

#Deskripsi
jenjang = str(input("masukan jenjang: "))
doktoral = ("Ilmu Komputer(FIK)")
pascasarjana = ("Magister Manajemen(FEB),Magister Teknik Informatika(FIK)")
sarjana = ("teknik Informatika, Sistem Informasi, DKV, Ilkom (FIK) Akuntansi Manajemen (FEB),English, Jepang (FIB),Kesehatan Masyarakat, Kesehatan Lingkungan (FKM),Eletro, Industri, Biomedis (FT)")
diploma4 = ("Animasi, Televisi (FIK),Perhotelan (FIB)")
diploma3 =("Teknik Informatika, Broadcasting (FIK),Rekam Medis (FKM)")
if(jenjang=="doktoral"):
    print(doktoral)
elif(jenjang=="pascasarjana"):
    print(pascasarjana)
elif(jenjang=="sarjana"):
    print(sarjana)
elif(jenjang=="diploma4"):
    print(diploma4)
elif(jenjang=="diploma3"):
    print(diploma3)
else:
    print("Tidak Valid")
