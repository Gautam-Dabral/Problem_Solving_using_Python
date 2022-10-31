def cutTheSticks(arr):
    # initializing result
    result = []
    result.append(len(arr))

    while len(arr)>0:

        m = min(arr)
        while m in arr:
            arr.remove(m)

        for items in arr:
            items -= m        
        
        if len(arr)>0:
            result.append(len(arr))

    return result

# initializing input - mapping str into int and converting into a list
arr = list(map(int, input().split()))

# join the result with next-line character \n 
res = '\n'.join(map(str, cutTheSticks(arr)))
print(res)