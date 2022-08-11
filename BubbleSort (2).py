def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = list(map(int,input("Masukan angka(pisahkan dengan spasi:").split()))

#before sorting
print("Bubble sort")
print("Before sorting:",arr)
#after sorting
bubbleSort(arr)
print ("After sorting:",arr)
