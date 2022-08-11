a = ["mangga","tomat","apel","jeruk","durian","manggis","semangka","sirsak","salak","pisang"]
b = ["rusa","kambing","sapi","jerapah","gajah","kerbau","kucing","harimau"]
c = ["fajar","rendi","samuel","rendra","deni","zidan","al","sekar","dhea","vanda","rifky","imanuel","riska"]
x = 1

print(a)
print(b)
print(c)

print("Elemen suku ke genapnya adalah:",end=" ")
for i in c:
    if(x%2 == 0):
        print(i, end=" ")
    x = x + 1
print()
x = x + 1

print(a[0])
print(a[9])
print(b[0])
print(b[7])
print(c[0])
print(c[12])

print("Variabel a")
print(a.pop())
print(a)
print("Variabel b")
print(b.pop())
print(b)
print("Variabel c")
print(c.pop())
print(c)
    
    

    
