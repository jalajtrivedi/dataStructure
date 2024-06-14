def linearSearch(arr, target):
    for index,element in enumerate(arr):
        if element==target:
            return index
    return -1

arr=[1,2,50,60,70,80]
target=70

a = linearSearch(arr,target)
if a!=-1:
    print("The index number is of the element",target,"is :",a)
else:
    print("elemnet is not in list")