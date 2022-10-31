#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l = []
    for char in s:
        if char != " ":
            l.append(char)
        else:
            l.append(' ')
    
    
    if l[0].isalpha():
        l[0] = l[0].upper()
        
    for i in range(1, len(l)):
        if l[i-1] == ' ' and l[i].isalpha():
            l[i] = l[i].upper()
            
    return str(''.join(l))        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
