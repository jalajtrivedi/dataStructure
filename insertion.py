def insertion(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [24,41,33,42,17]
insertion(arr)
print("Sorted array is:", arr)
