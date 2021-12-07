def quickSort(arr, left, right):
      if left < right:
        pos = partition(arr, left, right)
        quickSort(arr, left, pos - 1)
        quickSort(arr, pos + 1, right)

def partition(arr, left, right):
  pivot = arr[right]
  low = left - 1
  for i in range(left, right):
    if arr[i] <= pivot:
      low +=  1
      swap(arr,i,low)

  swap(arr,right,low+1)
  return low + 1


def swap(arr,i,low):
      arr[i], arr[low] = arr[low], arr[i]
      

if __name__ == "__main__":
    arr = [8,4,23,42,16,15]
    print(f"Array before sorted is {arr}")
    quickSort(arr,0,len(arr)-1)
    print(f"Array after sorted is {arr}")

