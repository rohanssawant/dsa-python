def merge(arr1, arr2, arr):
    """Merge two sorted `arr1` & `arr2` into `arr`"""
    print(f'do merge, arr1: {arr1}')
    print(f'do merge, arr2: {arr2}')
    print(f'do merge, before: {arr}')
    i = j = 0
    while i+j < len(arr):
        print(f'do merge, i: {i}')
        print(f'do merge, j: {j}')
        if j == len(arr2) or (i < len(arr1) and arr1[i] < arr2[j]):
            arr[i+j] = arr1[i]
            i += 1
        else:
            arr[i+j] = arr2[j]
            j += 1
        print(f'-----------ongoing merge, arr: {arr}-----------')
        
    print(f'-------end merge, after: {arr}-----')
    

def merge_sort(arr):
    print(f'in recursion: {arr}')
    n = len(arr)
    # Base case
    if n < 2:
        return
    
    # divide
    mid = n // 2

    arr1 = arr[0:mid]
    arr2 = arr[mid:n]

    # conquer
    merge_sort(arr1)
    merge_sort(arr2)
    print('--------------conquer ends------------------')

    # merge results
    merge(arr1, arr2, arr)
    
    return arr

array = [5,9,3,10]
print(merge_sort(array))