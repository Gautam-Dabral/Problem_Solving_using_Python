
def dton (n):
    num_string = 'zero one two three four five six seven eight nine'
    nums = num_string.split()
    num_d , i = {} , 0
    
    for items in nums:
        if items not in num_d.keys():
            num_d[items] = i
            i+=1
            
    digits , j = [] , 0

    while n>0:
        for keys in num_d.keys():
            if n%10 == num_d[keys]:
                digits.append(keys)
                n //= 10
    
    digits = digits[::-1]
    
    return (' '.join(digits))


print( dton(508345) )




