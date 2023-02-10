def secMax(l):
    if l == []: return None
    firMax, secMax = l[0], l[0]
    for i in range(len(l)):
        if l[i] < firMax and i==1:
            secMax = l[i]
        elif l[i] >= firMax:
            secMax, firMax = firMax, l[i]
        elif l[i] < firMax and l[i] > secMax:
            secMax = l[i] 
    return secMax

def secMin(l):
    if l == []: return None
    firMin, secMin = l[0], l[0]
    for i in range(len(l)):
        if l[i] > firMin and i==1:
            secMin = l[i]
        elif l[i] <= firMin:
            secMin, firMin = firMin, l[i]
        elif l[i] > firMin and l[i] < secMin:
            secMin = l[i] 
    return secMin
        
l1 = [5, 10, 20, 15]
l2 = [10, 20, 15, 2, 23, 90, 67]
l3 = [100, 80, 60, 50, 20]
l4 = [10, 20, 30, 40, 50]
l5 = [10,10,9,10,10]
l6 = []

print(secMax(l1), secMin(l1))
print(secMax(l2), secMin(l2))
print(secMax(l3), secMin(l3))
print(secMax(l4), secMin(l4))
print(secMax(l5), secMin(l5))
print(secMax(l6), secMin(l6))


