def rev(arr):
    for i in range(len(arr)//2):
        temp = arr[i]
        arr[i]= arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    return arr

print (rev([1,4,5,8,8,5,9,9,8,9,1000]))