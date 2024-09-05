'''In bubble sort, the largest value is bubbled up towards the end with every iteration.
In each iteration the two consecutive values are compared and swapped if  they not in order.
TC: O(n^2) SC: O(1)
'''

def bubble_sort(seq: list):
    for i in range(len(seq)):
        for j in range(len(seq)-i-1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq

seq = [5,9,3,10,45,2,0]
print(bubble_sort(seq))