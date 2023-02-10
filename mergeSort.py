import sys
sys.setrecursionlimit(10000)

def merge(l1, l2):
    merged = []
    i, j = 0, 0
    while (i+j < len(l1)+len(l2)):
        if i<len(l1) and j<len(l2):
            if l1[i] <= l2[j]:
                merged.append(l1[i])
                i += 1
            else:
                merged.append(l2[j])
                j += 1
        if i == len(l1) and j<len(l2):
            merged.append(l2[j])
            j += 1
        if j == len(l2) and i<len(l1):
            merged.append(l1[i])
            i += 1
    return merged

def mergeSort (A,l,r):
    if r-l <= 1: return A[l:r]
    if r-l > 1:
        mid = (l+r)//2
        left = mergeSort(A, l, mid)
        right = mergeSort(A, mid, r)
    return merge(left, right)

l = [1,3,2,5,4,7,9,2,5]
print(mergeSort(l,0,len(l)))
