def costliest (a):
    max_total = 0
    for i in range(len(a)):
        total = a[i]
        for j in range(i, len(a)-1):
            if a[j]<a[j+1]:
                total += a[j+1]
            else:
                break
        if max_total < total:
            max_total = total
    return max_total

arr = list(map(int, input().split(' ')))
print(costliest(arr))
# 12 2 3 5 7 5 10 8 9 