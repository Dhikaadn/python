data_angka = list(map(int,input("Masukan angka(pisahkan dengan spasi:").split()))
cek = int(input('Masukkan angka yang ingin dicocokkan: '))
print(data_angka)
jml_data = len(data_angka)-1
for i in range(jml_data):
       for j in range(jml_data):
               if  data_angka[j] < data_angka[j+1]: #Max sort : mengubah tanda > menjadi <
                   data_angka[j],data_angka[j+1] = data_angka[j+1],data_angka[j] 
print(data_angka)

if cek in data_angka:
          print('ada')
else:
       print('tidak ada')



