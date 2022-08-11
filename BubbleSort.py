data_angka = [12, 14, 19, 21, 22, 34, 52, 62, 23, 17, 52]
print(data_angka)
jml_data = len(data_angka)-1
for i in range(jml_data):
       for j in range(jml_data):
               if  data_angka[j] > data_angka[j+1]:
                   data_angka[j],data_angka[j+1] = data_angka[j+1],data_angka[j] 
print(data_angka)
