def BinarySeach(array,left,right,x):
    if right>=left:
        mid=(left+right)//2

        if array[mid]==x:
            return mid
        elif array[mid]>x:
            return BinarySeach(array,left,mid-1,x)
        else:
            return BinarySeach(array,mid+1,right,x)
    else:
        return -1

array = [1,2,4,5,7,8]
x=7
result = BinarySeach(array,0,len(array)-1,x)
if result == -1:
    print("Number is not in the array")
else:
    print("The number is in index:",str(result))