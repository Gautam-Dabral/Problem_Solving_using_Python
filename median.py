import sys

sys.setrecursionlimit(100000)


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i,j,k = 0,0,l     

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
    return arr

def findMedian(arr):
    # Write your code here
    arr_sorted = mergeSort(arr, 0, len(arr)-1)
    #print(arr)
    #print(arr_sorted)
    return (arr_sorted[(len(arr)+1)//2])
    



arr = [0, 3, 2, 1, 5 ,6 ,6, 8, 3, 7]

print(findMedian(arr))