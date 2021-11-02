def binarySearch(arr,val):
    low = 0
    high = len(arr) -1
    index = -1

    while (low < high):
        middle = (low + high) // 2
        if arr[middle] == val:
            index = middle 
            break
        if (arr[middle] < val):
            low = middle +1
        else:
            high = middle -1

    return index

print(binarySearch([1,2,3,4,5,6,7,8,9,10,15,25,55],5))