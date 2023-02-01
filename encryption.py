import math
import os
import random
import re
import sys

# An English text needs to be encrypted using the following encryption scheme.
# First, the spaces are removed from the text. Let l be the length of this text.
# Then, characters are written into a grid, whose rows and columns have the following constraints:
# row <= floor(sqrt(len(string))) <= col <= ceil(sqrt(len(string)))
# rows x cols >= len(string)
# If multiple grids satisfy the above conditions, choose the one with the minimum area, rows x cols.
# TC1 - if god wanted us to stay on ground he would have given us roots
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    strr = ''.join(s.split(' '))
    l = len(strr)
    row , col = math.floor(math.sqrt(l)), 0
    arr = [] 
    k = 0
    for j in range(row):
        if col == 0:
            col += math.ceil(math.sqrt(l))
        else :
            k += col
            col += math.ceil(math.sqrt(l))
        temp_arr = [strr[i] for i in range(k, col)]
        arr.append(temp_arr)
        
    return arr

if __name__ == '__main__':

    s = input("Enter the string to encrypt : ")

    result = encryption(s)

    print(result)
    print(" rows : ", len(result))
    print(" cols : ", len(result[0]))

