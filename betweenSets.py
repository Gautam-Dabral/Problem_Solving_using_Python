import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#  It returns no of integers between the two sets, such that,
#  1. The elements of the first array are all factors of the integer being considered
#  2. The integer being considered is a factor of all elements of the second array 

def getTotalX(a, b):

    btwlist = 0
    
    for btw in range(a[-1], b[0]+1, a[-1]):
        for items in a:
            if btw % items != 0:
                break
        else:
            for items in b:
                if items % btw != 0:
                    break
            else:
                btwlist += 1
    
    return btwlist
                      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
