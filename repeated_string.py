#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    
    if n <= len(s):
        return ( s[:n+1].count('a') )
    else:
        r = n%len(s)
        non_r = n - r
        a1 = s[:r].count('a')
        a2 = s.count('a') * (non_r // len(s))
        
    return  (a1+a2)
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
