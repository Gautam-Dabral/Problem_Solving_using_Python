from math import sqrt

def squarebetween (a, b):
    count = 0

    for num in range(int(sqrt(a)) , int(sqrt(b))+1):
        if int(num*num) in range(a,b+1):
            count += 1
        
    return count

print(squarebetween(4, 49))
            