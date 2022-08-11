a = ["mangga","tomat","apel","jeruk","durian","manggis","semangka","sirsak","salak","pisang"]
b = ["rusa","kambing","sapi","jerapah","gajah","kerbau","kucing","harimau"]
c = ["anak ke-2 fajar","anak ke-2 rendi","anak ke-2 samuel","anak ke-1 vicky","anak ke-1 deni","anak ke-2 zidan","anak ke-1 al","anak ke-3 sekar","anak ke-3 dhea","anak ke-1 vanda","anak ke-1 rifky","anak ke-1 imanuel","anak ke-2 riska"]
x = 1
# Menampilkan Ketiga Data List Tersebut
print("var a:",a)
print("var b:",b)
print("var c:",c)

# Menampilkan Data 3(Variabel c) dengan Suku ke Genap
print("Elemen suku ke genapnya adalah:",end=" ")
for i in c:
    if(x%2 == 0):
        print(i, end=" ")
    x = x + 1
print()
x = x + 1

# Menampilkan Data Pertama dan Terakhir dari Ketiga List Tersebut
print("Variabel a")
print("Data pertama:",a[0])
print("Data terakhir:",a[9])
print("Variabel b")
print("Data pertama:",b[0])
print("Data terakhir:",b[7])
print("Variabel c")
print("Data pertama:",c[0])
print("Data terakhir:",c[12])

# Menghapus Elemen Terakhir dari Ketiga List Tersebut
print("Variabel a")
print(a.pop())
print(a)
print("Variabel b")
print(b.pop())
print(b)
print("Variabel c")
print(c.pop())
print(c)
    
    

    
     
