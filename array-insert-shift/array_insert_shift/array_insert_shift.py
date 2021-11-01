def insertShiftArray(arr,value):
    if len(arr) == 0 or len(arr) == 1:
        arr.append(value)
        return arr
    if len(arr) % 2 == 0:
        middle = len(arr)//2
    else:
        middle = len(arr)//2+1
    
    temp = arr[middle]
    arr[middle] = value
    for i in range(middle+1,len(arr)):
        temp1 = temp
        temp = arr[i]
        arr[i] = temp1
    arr.append(temp)
    return arr