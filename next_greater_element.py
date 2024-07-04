def next_greater_element(arr):
    stack = []
    for i in range(len(arr)):
        
        while stack and stack[-1] < arr[i]:
            print(stack.pop(), "-->", arr[i])

        
        stack.append(arr[i])

    
    while stack:
        print(stack.pop(), "-->", -1)



arr = [5,8,3,7,4,9]
next_greater_element(arr)