def selection_sort(arr):
    for i in range(len(arr)):
        curr_min = arr[i]
        curr_min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < curr_min:
                curr_min = arr[j]
                curr_min_index = j
        arr[curr_min_index], arr[i] = arr[i], arr[curr_min_index]
    return arr

array = [5,9,3,10,45,2,0] 
print(selection_sort(array))
