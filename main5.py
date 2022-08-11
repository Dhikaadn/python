import prak5
#Kasus 1,2,3
def main():
    A = [5,2,10,27,33]
    l = len(A)
    print(prak5.InsertionSortAscending(l,A))
    print(prak5.InsertionSortDescending(l,A))
    print(prak5.input3int(A))
    B = [15,12,20,50,100]
    print(B)
    Bsort=prak5.kasus31(B)
    print(Bsort)
    Bmodif=prak5.kasus32(Bsort)
    print(Bmodif)
    
    
main()
