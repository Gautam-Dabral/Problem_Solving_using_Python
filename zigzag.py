from array import array
from math import floor
def findZigZagSequence(a, n):
    a = sorted(a)
    mid = floor(n/2)
    a[mid], a[n-1] = a[n-1], a[mid]
    print(a)
    start = mid + 1
    end = n - 2
    while(start <= end):
        a[start], a[end] = a[end], a[start]
        start = start + 1
        end = end - 1

    for i in range (n):
        print(a[i], end = ' ')

arr = array('i', [1,2,3,4,5,6,7,8])
findZigZagSequence(arr, len(arr))