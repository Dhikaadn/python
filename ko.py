n = int(input(""))
if n > 0:
    if n%2==0:
        print("positif genap")
    else:
        print("positif ganjil")
elif n < 0:
    if n%2==0:
        print("negatif genap")
    else:
        print("negatif ganjil")
else:
    print("nol")

