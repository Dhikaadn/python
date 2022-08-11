

#python
# Kamus
arrUsia = [int]*7
i = 0
jamak = False
ketemu = False

# Algoritma

# Inputkan usia
while i<len(arrUsia):
    arrUsia[i]=int(input("Usia ke-"+str(i+1)+":"))
    i=i+1
print(end="")

# Outputkan usia
while i<len(arrUsia):
    print(arrUsia[i],end="")
    i = i+1
cari = int(input("masukan usia yang ingin dicari: "))
for index in range(len(arrUsia)):
    if arrUsia[index]==cari:
        if not jamak:
            print("Usia ke-" +str(cari),"berada pada data ke-"+str(index+1),end="")
            jamak = True
            ketemu = True
        else:
            print(",ke-"+str(index+1),end="")
if not ketemu:
    print("Usia tidak ditemukan")
