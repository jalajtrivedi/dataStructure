def bubble(arr1):
    n = len(arr1)
    
    for i in range(n):
        swapped = (False)
        for j in range(0,n-i-1):
            if arr1[j]>arr1[j+1]:
                arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
                swapped=True
        if not swapped:
            break
            
            
arr1 = [24,41,33,42,17]
bubble(arr1)
print(arr1)