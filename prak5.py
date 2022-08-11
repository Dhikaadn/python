#Kasus 4
#var global
AId=[]
ABrg=[]
AHrg=[]

def InputData(arrId,arrBarang,arrHarga,n):
    for i in range(n):
        AId.append(arrId[i])
        ABrg.append(arrBarang[i])
        AHrg.append(arrHarga[i])
def LihatData(n):
    print("ID NAMA BARANG HARGA")
    for i in range(n):
        print(AId[i],ABrg[i],AHrg[i])
def LihatDataTerurut(n):
    tempid = 0
    tempNama = ""
    tempHarga = 0
    for i in range(1,n):
        tempid = AId[i]
        tempNama = ABrg[i]
        tempHarga = AHrg[i]
        j = i-1
        while j>=0 and tempid < AId[j]:
            AId[j+1] = AId[j]
            ABrg[j+1] = ABrg[j]
            AHrg[j+1] = AHrg[j]
            j = j-1
        AId[j+1]=tempid
        ABrg[j+1]=tempNama
        AHrg[j+1]=tempHarga
    print("ID NAMA BARANG HARGA")
    for i in range(n):
        print(AId[i],ABrg[i],AHrg[i])

#Kasus 1
def InsertionSortAscending(n,A):
    temp = 0
    for i in range(1,n):
        temp = A[i]
        j = i-1
        while j>=0 and temp < A[j]:
            A[j+1] = A[j]
            j = j-1
        A[j+1]=temp
    return A

def InsertionSortDescending(n,A):
    temp = 0
    for i in range(1,n):
        temp = A[i]
        j = i-1
        while j>=0 and temp > A[j]:
            A[j+1] = A[j]
            j = j-1
        A[j+1]=temp
    return A
#Kasus 2
def input3int(A):
    print("Masukkan bilangan 1: ",end=" ")
    A.append(int(input()))
    print("Masukkan bilangan 2: ",end=" ")
    A.append(int(input()))
    print("Masukkan bilangan 3: ",end=" ")
    A.append(int(input()))
    InsertionSortAscending(len(A),A)
    return A
#Kasus 3
def kasus31(B):
    l = len(B)
    el = B[0]
    if el%2==0:
        for i in range(l):
            B[i]=B[i]*2
        B=InsertionSortAscending(l,B)
    else:
        for i in range(l):
            B[i]=B[i]*3
        B=InsertionSortDescending(l,B)
    return B

def kasus32(B):
    l = len(B)
    i0 = B[0]
    i1 = B[l-1]
    urut="asc"
    if i0>i1:
        urut="desc"
    print("masukkan bilangan untuk mengubah B[0]:",end="")
    B[0]=int(input())
    if urut=="asc":
        if B[0]>B[1]:
            B=InsertionSortAscending(l,B)
    else:
        if B[0]<B[1]:
            B=InsertionSortDescending(l,B)
    return B
            
