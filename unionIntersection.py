def union(l1,l2):
    l = l1[:]
    for i in range(len(l2)):
        if l2[i] not in l:
            l.append(l2[i])
            for j in range(len(l)-1,-1,-1):
                if j > 0 and l[j] < l[j-1]:
                    l[j], l[j-1] = l[j-1], l[j]
    return l

def intersection(l1,l2):
    l = l1[:]
    for item in l1:
        if item in l and item not in l2:
            l.remove(item)
    return l

l1 = [1,2,3,5,7]
l2 = [2,3,6,9]

print(union(l1, l2))
print(intersection(l1, l2))