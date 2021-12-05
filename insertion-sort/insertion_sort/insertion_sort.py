def insertion_sort(arr):
    if len(arr) == 0:
        raise Exception('Empty list')
    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]
        while j >= 0  and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j + 1] = temp

if __name__ == "__main__":
    arr1 = [8,4,23,42,16,15]
    print(f"Array before sorting {arr1}")
    insertion_sort(arr1)
    print(f"Array after sorting {arr1}")

    arr2 = [20,18,12,8,5,-2]
    print(f"Array before sorting {arr2}")
    insertion_sort(arr2)
    print(f"Array after sorting {arr2}")

    arr3 = [5,12,7,5,5,7]
    print(f"Array before sorting {arr3}")
    insertion_sort(arr3)
    print(f"Array after sorting {arr3}")

    arr4 = [2,3,5,7,13,11]
    print(f"Array before sorting {arr4}")
    insertion_sort(arr4)
    print(f"Array after sorting {arr4}")
