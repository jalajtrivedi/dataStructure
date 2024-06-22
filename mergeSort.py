def merge(left,right):
    new =[]
    i,j =0,0
    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
    
    new.extend(left[i:])
    new.extend(right[j:])
    return new
    
        

def mergeSort(arr):
    if len(arr)<=1:
        return arr 
    mid = len(arr)//2
    l_half = arr[:mid]
    r_half = arr[mid:]
    l_half = mergeSort(l_half)
    r_half = mergeSort(r_half)
    
    return merge(l_half,r_half)

arr=[77,66,55,14,33,2,11,1]
arr1 = mergeSort(arr)
print(arr1)