a = [10,5,25,6,8,12,14]
largest = a[0]
smallest= a[0]
for num in a:
    if num>largest:
        largest=num
    elif num<smallest:
        smallest = num

print("the largest number is ", largest)
print ("the smallest number is ", smallest)
