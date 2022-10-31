
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
# It returns the absolute diagonal diff between the sun of both diagonals ( 'l to r' & 'r to l')

def diagonalDifference(arr):
    # Write your code here
    ltrd , rtld = 0 , 0
    for i in range(len(arr[0])):
        ltrd += arr[i][i]
        rtld += arr[i][len(arr[0])-1-i]
        
    return (abs(ltrd-rtld))