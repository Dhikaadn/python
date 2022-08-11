n = "Y"
while (n == "Y"):
    print (70*"=")
    print ("Pengisisan Data KTP")
    print ("Mohon Untuk Mengisi Data di Bawah Ini Dengan Benar!\n")
    nik = int(input("NIK                : "))
    nama = str(input("Nama               : "))
    tmpt_lhr = str(input("Tempat lahir       : "))
    tgl = input("Tanggal lahir      : ")
    bln = input("Bulan lahir        : ")
    thn = input("Tahun lahir        : ")
    jns_klm = str(input("Jenis kelamin      : "))
    goldar = input ("Gol.darah          : ")
    almt = input("Alamat             : ")
    rt = int(input("RT                 : "))
    rw = int(input("RW                 : "))
    kel_des = input("Kel/Desa           : ")
    kec = input("Kecamatan          : ")
    agama = input ("Agama              : ")
    sts = input ("Status perkawinan  : ")
    pkj = input ("Pekerjaan          : ")
    kwrg = str(input("Kewarganegaraan    : "))
    brlk = str(input("Berlaku hingga     : "))
#=================================================================================
    n =str(input("Ingin mengisi data lagi?(Y/T)"))
#output
print (70*"=")
print ("\t\t     PROVINSI JAWA TENGAH")
print ("\t\t\tKOTA SEMARANG\n")
print ("NIK                 :",nik)
print ("Nama                :",nama)
print ("Tempat/Tgl Lahir    :",str(tmpt_lhr)+",",str(tgl)+"-"+str(bln)+"-"+str(thn))  
print ("Jenis Kelamin       :",jns_klm,"\tGol.Darah :",goldar)
print ("Alamat              :",almt)
print ("\tRT/RW       :",str(rt)+"/"+str(rw))
print ("\tKel/Desa    :",kel_des)
print ("\tKecamatan   :",kec)
print ("Agama               :",agama)
print ("Status Perkawinan   :",sts)
print ("Pekerjaan           :",pkj)
print ("Kewarganegaraan     :",kwrg)
print ("Berlaku Hingga      :",brlk)
print (70*"=")





    
