a=[5,10,25,6,8,12,14]
target = 35
num_index={}
found = False

for i , num in enumerate(a):
    complement= target-num
    if complement in num_index:
        print("the index of two is ",num_index[complement], "and",i )
        print("number",a[num_index[complement]], "and", num)
        found = True
        break
    num_index[num]=i