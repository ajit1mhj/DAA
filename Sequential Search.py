def BinarySearch(array,n,x):
    for i in range(0,x):
        if(array[i]==x):
            return i
    return -1

array = [15,5,20,35,2,42,67,17]
x=42
n=len(array)
result = BinarySearch(array,n,x)

if(result==-1):
    print("Element is not in the array")
else:
    print("Element is at index: ",result)