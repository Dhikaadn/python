def selection(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j     
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = list(map(str,input("Masukan angka(pisahkan dengan spasi):").split()))
#before sorting
print("Selection sort")
print("Before sorting:",arr)
#after sorting
selection(arr)
print ("After sorting:",arr)
