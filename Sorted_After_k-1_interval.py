def switch(k,l,l2):
    count, ans = 0, False
    for i in range(len(l)):
        if i+k < len(l) and l[i] > l[i+k]:
            l[i], l[i+k] = l[i+k], l[i]
            count += 1
    if count == 0:
        if l == l2:
            ans = True
    elif count > 0:
        if l == l2:
            ans = True
        else:
            ans = switch(k,l,l2)
    
    return ans

k = 1
l = [3,2,6,7,9,5]
l2 = sorted(l)
print(switch(k,l,l2))