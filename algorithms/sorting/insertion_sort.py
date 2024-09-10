def insertion_sort(arr):
    for i in range(1, len(arr)):
        print(arr)
        curr = arr[i]
        if curr < arr[i-1]:
            for j in range(i-1, -1, -1):
                if curr > arr[j]:
                    arr[j+1] = curr
                    break
                else:
                    if j == 0:
                        arr[j+1] = arr[j]
                        arr[j] = curr
                    else:
                        arr[j+1] = arr[j]           # Shift ele
    
    return arr

array = [5,9,3,10,45,2,0]
print(insertion_sort(array))