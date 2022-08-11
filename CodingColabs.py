print("No 1")
for i in range(10):
  for j in range(10):
    print("%3d" % ((j+1)*(i+1)), end=" ")
  print()

print("No 2")
# List = 
# List, Tuple, Dictionary, Set

list_nilai = [45, 87, 90, 76]
list_kosong = []
list_string = ["Bambang", "Makan", "Bakso"]
list_campur = [43, 78.98, "Nama", True]

idx = 0
while idx < len(list_nilai):
  print(list_nilai[idx], end=" ")
  idx += 1
print()
for nama in list_string:
  print(nama, end=" | ")
print()
for data in list_campur:
  print(data, end=" | ")

print("No 3")
data_angka = [12, 14, 19, 21, 22, 34, 52, 62, 23, 17, 52]
print(data_angka[0])
print(data_angka[-1])
print(data_angka[5])

data_angka[5] = 100
data_angka[-1] = 200
data_angka[-2] = 240
print(data_angka)

data_angka.remove(52)
print(data_angka)

data_angka.pop()
print(data_angka)

data_angka.pop(2)
print(data_angka)

print("No 4")
data_angka = [12, 14, 19, 21, 22, 34, 52, 62, 23, 17, 52]

data_angka.append(1)
print(data_angka)

data_angka.insert(4, 500)
print(data_angka)

print("No 5")
list_1 = [8, 48, 14, 37, 49, 12, 18, 7, 49, 28]
list_2 = [23, 14, 31, 25, 29, 33, 23, 2, 7, 15]
list_1.sort(reverse=True)
print(list_1)
#list_2.reverse()
#print(list_2)
 
print(list_2[::-1])

print("No 6")
data_angka = [12, 14, 19, 21, 22, 34, 52, 62, 23, 17, 52]

print(data_angka[5:9])
print(data_angka[:9])
print(data_angka[5:])

print("No 7")
#matrik 2x2
matrix = [
    [5, 0],
    [2, 6],
]

for x in range(0, len(matrix)):
    for y in range(0, len(matrix[0])):
        print (matrix[x][y], end=' '),
    print
