
def senslope_ (l):

    slope_l = []
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            slope_l.append((l[j]-l[i])//(j-i))

    slope_l.sort()
    print(slope_l)

    if len(slope_l)%2 != 0:
        senslope = slope_l[(len(slope_l)+1)//2]
    else:
        senslope =  ( slope_l[len(slope_l)//2] + slope_l[(len(slope_l)+1)//2] ) // 2
    
    return senslope

l = [56,98,12,20,67,12,29,48,88,96,55]

print(senslope_(l))