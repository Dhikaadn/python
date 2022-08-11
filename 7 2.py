n = int(input("jumlah segitiga: "))
for i in range(n):
    t = int(input("jumlah baris segitiga"))
    for num in range(t+1):
        for j in range(num):
            print(num,end=" ")
        print("\n")
