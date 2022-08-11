def tambah(a,b,c,d):
    return a+b+c+d
def kurang(a,b,c,d):
    return a-b-c-d
def kali(a,b,c,d):
    return a*b*c*d
def bagi(a,b,c,d):
    return a/b/c/d
def banding(a,b,c,d):
    if a>b and a>c and a>d:
        print("angka pertama terbesar")
    elif b>a and b>c and b>d:
        print("angka kedua terbesar")
    elif c>a and c>b and c>d:
        print("angka ketiga terbesar")
    elif d>a and d>b and d>c:
        print("angka keempat terbesar")
    else:
        print("tidak ada yang terbesar")
        
