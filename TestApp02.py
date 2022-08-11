from mylib02 import*
def main():
    x = int(input("Masukkan sisi:"))
    print("luas:",luas(x))
    print("keliling:",keliling(x))
    print("volume:",volume(x))
    #tes sisi positif negatif
    if x>0:
        print("sisi termasuk bilangan positif")
    elif x<0:
        print("sisi termasuk bilangan negatif")
    else:
        print("nol")
    #tes sisi ganjil genap
    if x%2==0:
        print("sisi termasuk bilangan genap")
    else:
        print("sisi termasuk bilangan ganjil")
    #tes luas positif negatif
    if luas(x)>0:
        print("luas termasuk bilangan positif")
    elif luas(x)<0:
        print("luas termasuk bilangan negatif")
    else:
        print("nol")
    #tes luas ganjil genap
    if luas(x)%2==0:
        print("luas termasuk bilangan genap")
    else:
        print("luas termasuk bilangan ganjil")   
    #tes keliling positif negatif
    if keliling(x)>0:
        print("keliling termasuk bilangan positif")
    elif keliling(x)<0:
        print("keliling termasuk bilangan negatif")
    else:
        print("nol")
    #tes keliling ganjil genap
    if keliling(x)%2==0:
        print("keliling termasuk bilangan genap")
    else:
        print("keliling termasuk bilangan ganjil")
main()
